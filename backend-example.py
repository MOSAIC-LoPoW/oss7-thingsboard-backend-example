#!/usr/bin/env python

from __future__ import print_function
import argparse
import socket
import subprocess

from datetime import datetime
import jsonpickle
import serial
import time

import paho.mqtt.client as mqtt
import signal

import struct

from d7a.alp.command import Command
from d7a.alp.operations.responses import ReturnFileData
from d7a.system_files.system_file_ids import SystemFileIds
from d7a.system_files.system_files import SystemFiles
from modem.modem import Modem

import time
from pprint import pprint

from tb_api_client import swagger_client
from tb_api_client.swagger_client import ApiClient, Configuration
from tb_api_client.swagger_client.rest import ApiException


class BackendExample:
  def __init__(self):
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-v", "--verbose", help="verbose", default=False, action="store_true")
    argparser.add_argument("-b", "--broker", help="mqtt broker hostname", default="localhost")
    argparser.add_argument("-u", "--url", help="URL of the thingsboard server", default="http://localhost:8080")
    argparser.add_argument("-t", "--token", help="token to access the thingsboard API", required=True)
    self.mq = None
    self.connected_to_mqtt = False

    self.config = argparser.parse_args()
    self.connect_to_mqtt()

    api_client_config = Configuration()
    api_client_config.host = self.config.url
    api_client_config.api_key['X-Authorization'] = self.config.token
    api_client_config.api_key_prefix['X-Authorization'] = 'Bearer'
    api_client = ApiClient(api_client_config)

    self.device_controller_api = swagger_client.DeviceControllerApi(api_client=api_client)
    self.device_api_controller_api =swagger_client.DeviceApiControllerApi(api_client=api_client)

  def connect_to_mqtt(self):
    self.connected_to_mqtt = False

    self.mq = mqtt.Client("", True, None, mqtt.MQTTv31)
    self.mq.on_connect = self.on_mqtt_connect
    self.mq.on_message = self.on_mqtt_message
    self.mq.connect(self.config.broker, 1883, 60)
    self.mq.loop_start()
    while not self.connected_to_mqtt: pass  # busy wait until connected
    print("Connected to MQTT broker on {}".format(
      self.config.broker,
    ))

  def on_mqtt_connect(self, client, config, flags, rc):
    self.mq.subscribe("/tb")
    self.connected_to_mqtt = True

  def on_mqtt_message(self, client, config, msg):
    # msg contains already parsed command in ALP in JSON
    print("ALP Command received from TB: {}".format(msg.payload))
    try:
      obj = jsonpickle.json.loads(msg.payload)
    except:
      print("Payload not valid JSON, skipping") # TODO issue with TB rule filter, to be fixed
      return

    gateway = obj["deviceId"]
    cmd = jsonpickle.decode(jsonpickle.json.dumps(obj["alp"]))
    node_id = gateway  # overwritten below with remote node ID when received over D7 interface
    # get remote node id (when this is received over D7 interface)
    if cmd.interface_status != None and cmd.interface_status.operand.interface_id == 0xd7:
      node_id = '{:x}'.format(cmd.interface_status.operand.interface_status.addressee.id)

    # look for returned file data which we can parse, in this example file 64
    my_sensor_value = 0
    for action in cmd.actions:
      if type(action.operation) is ReturnFileData and action.operand.offset.id == 64:
        my_sensor_value = struct.unpack("L", bytearray(action.operand.data))[0] # parse binary payload (adapt to your needs)
        print("node {} sensor value {}".format(node_id, my_sensor_value))

    # save the parsed sensor data as an attribute to the device, using the TB API
    try:
      # first get the deviceId mapped to the device name
      response = self.device_controller_api.get_tenant_device_using_get(device_name=str(node_id))
      device_id = response.id.id

      # next, get the access token of the device
      response = self.device_controller_api.get_device_credentials_by_device_id_using_get(device_id=device_id)
      device_access_token = response.credentials_id

      response = self.device_api_controller_api.post_device_attributes_using_post(
        device_token=device_access_token,
        json={ "my_sensor": my_sensor_value }
      )

      print("Updated my_sensor attribute for node {}".format(node_id))
    except ApiException as e:
      print("Exception when calling API: %s\n" % e)


  def __del__(self):
    try:
      self.mq.loop_stop()
      self.mq.disconnect()
    except:
      pass

  def run(self):
    print("Started")
    keep_running = True
    while keep_running:
      try:
        signal.pause()
      except KeyboardInterrupt:
        print("received KeyboardInterrupt... stopping processing")
        keep_running = False


if __name__ == "__main__":
  BackendExample().run()
