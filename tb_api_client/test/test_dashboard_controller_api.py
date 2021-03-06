# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.dashboard_controller_api import DashboardControllerApi


class TestDashboardControllerApi(unittest.TestCase):
    """ DashboardControllerApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.dashboard_controller_api.DashboardControllerApi()

    def tearDown(self):
        pass

    def test_assign_dashboard_to_customer_using_post(self):
        """
        Test case for assign_dashboard_to_customer_using_post

        assignDashboardToCustomer
        """
        pass

    def test_assign_dashboard_to_public_customer_using_post(self):
        """
        Test case for assign_dashboard_to_public_customer_using_post

        assignDashboardToPublicCustomer
        """
        pass

    def test_delete_dashboard_using_delete(self):
        """
        Test case for delete_dashboard_using_delete

        deleteDashboard
        """
        pass

    def test_get_customer_dashboards_using_get(self):
        """
        Test case for get_customer_dashboards_using_get

        getCustomerDashboards
        """
        pass

    def test_get_dashboard_by_id_using_get(self):
        """
        Test case for get_dashboard_by_id_using_get

        getDashboardById
        """
        pass

    def test_get_dashboard_info_by_id_using_get(self):
        """
        Test case for get_dashboard_info_by_id_using_get

        getDashboardInfoById
        """
        pass

    def test_get_server_time_using_get(self):
        """
        Test case for get_server_time_using_get

        getServerTime
        """
        pass

    def test_get_tenant_dashboards_using_get(self):
        """
        Test case for get_tenant_dashboards_using_get

        getTenantDashboards
        """
        pass

    def test_get_tenant_dashboards_using_get1(self):
        """
        Test case for get_tenant_dashboards_using_get1

        getTenantDashboards
        """
        pass

    def test_save_dashboard_using_post(self):
        """
        Test case for save_dashboard_using_post

        saveDashboard
        """
        pass

    def test_unassign_dashboard_from_customer_using_delete(self):
        """
        Test case for unassign_dashboard_from_customer_using_delete

        unassignDashboardFromCustomer
        """
        pass


if __name__ == '__main__':
    unittest.main()
