# Introduction

This project is closely related to the [oss7-thingsboard-gateway](https://github.com/MOSAIC-LoPoW/oss7-thingsboard-gateway) project, which allows to integrate an OSS-7 gateway with [ThingsBoard](https://github.com/thingsboard/thingsboard).
This project builds on top of the gateway and ThingsBoard platform and show how to build an application on top of this platform.
Thingsboard is configured to forward all DASH7 ALP commands to an external MQTT broker. This example subscribes to this broker and parser the ALP commands.
The parsing happens here so we don't need to integrate the business logic and parsing logic in ThingsBoard. However, after the sensor value is parsed it is 
stored as an attribute attached to the device in ThingsBoard using it's API. In this way ThingsBoard contains all data (ie a digital twin of the devices).

# Installation

- clone the repository, including the submodules: `$ git clone --recurse-submodules https://github.com/MOSAIC-LoPoW/oss7-thingsboard-backend-example.git`
- install the requirements: `$ sudo pip2 install -r requirements.txt`

# Running 

    $ PYTHONPATH=lib/pyd7a/ python2 backend-example.py --help
    usage: backend-example.py [-h] [-v] [-b BROKER] [-u URL] -t TOKEN
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         verbose
      -b BROKER, --broker BROKER
                            mqtt broker hostname
      -u URL, --url URL     URL of the thingsboard server
      -t TOKEN, --token TOKEN
                            token to access the thingsboard API
                            
The example will parse the sensor data as transmitted by OSS-7 sensor nodes by default, and store this in the `my-sensor` of the device.
