import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Utilities.login_excel_reader import ExcelFunction
from Utilities.test_executor import perform_excel_login_test
from PageObjects.locator_ddt import LocatorDDT
from PageObjects.login_page import LoginPages
from Configurations.conftest import driver_setup
from TestDatas.data import Data
from PageObjects.inventory_page import InventoryPage



class Test_ECommerce:
    def test_login_ddt(self, driver_setup):
        excel = ExcelFunction(Data.excel_file, Data.sheet_name)
        rows = excel.row_count()
        perform_excel_login_test(driver_setup, excel,rows,Data,LocatorDDT)