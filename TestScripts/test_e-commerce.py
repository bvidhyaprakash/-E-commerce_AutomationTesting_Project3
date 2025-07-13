from time import sleep

import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Utilities.login_excel_reader import ExcelFunction
from Utilities.test_executor import perform_excel_login_test
from PageObjects.locator_ddt import LocatorDDT
from TestDatas.data import Data
from PageObjects.login_page import LoginPages
from PageObjects.inventory_page import InventoryPage
from PageObjects.cart_page import CartPage
from PageObjects.checkout_page import CheckoutPage
from Configurations.conftest import driver_setup
from Keywords.keywords_engine import KeywordEngine



class Test_ECommerce:
    def test_login_ddt(self, driver_setup):
        excel = ExcelFunction(Data.excel_file, Data.sheet_name)
        rows = excel.row_count()
        perform_excel_login_test(driver_setup, excel,rows,Data,LocatorDDT)

    def test_invalid_login(self, driver_setup):
        driver_setup.get(Data.url)
        login = LoginPages(driver_setup)
        login.login(Data.invalid_username, Data.invalid_password)
        login.is_login_error_displayed() #checking the error message displayed for invalid login

    def test_logout(self, driver_setup):
        driver_setup.get(Data.url)
        login = LoginPages(driver_setup)
        login.login(Data.valid_username, Data.valid_password)
        sleep(2)
        inventory = InventoryPage(driver_setup)
        inventory.logout()
        assert "saucedemo.com" in driver_setup.current_url # checking the current url once logout

    def test_cart_keyword_driven(self, driver_setup):
        yaml_path = os.path.join(os.path.dirname(__file__), "..", "configurations", "testdata.yaml")
        engine = KeywordEngine(driver_setup, yaml_path)
        engine.run_steps()

    def test_add_to_cart_and_validate(self, driver_setup):
        driver_setup.get(Data.url)
        login = LoginPages(driver_setup)
        login.login(Data.valid_username, Data.valid_password)
        inventory = InventoryPage(driver_setup)
        inventory.add_to_cart_by_index(0)
        inventory.add_to_cart_by_index(1)
        sleep(2)
        cart_text = inventory.get_inventory_count_text()
        assert cart_text == "2" # checking the item count added in the cart list

    def test_cart_items(self, driver_setup):
        driver_setup.get(Data.url)
        login = LoginPages(driver_setup)
        login.login(Data.valid_username, Data.valid_password)
        inventory = InventoryPage(driver_setup)
        inventory.add_to_cart_by_index(0)
        inventory.open_cart()
        sleep(3)
        cart = CartPage(driver_setup)
        items = cart.get_cart_items()
        sleep(3)
        assert "Sauce Labs Backpack" in items # checking the item added in the card list

    def test_checkout_order(self, driver_setup):
        driver_setup.get(Data.url)
        login = LoginPages(driver_setup)
        login.login(Data.valid_username, Data.valid_password)

        inventory = InventoryPage(driver_setup)
        inventory.add_to_cart_by_index(0)
        inventory.open_cart()
        sleep(3)
        checkout = CheckoutPage(driver_setup)
        checkout.perform_checkout(Data.perform_checkout_fname, Data.perform_checkout_lname, Data.perform_checkout_postal_no)
        sleep(3)
        assert checkout.get_confirmation_message() == "Thank you for your order!" # checking the success message

    def test_sort_by_price_low_to_high(self, driver_setup):
        driver_setup.get(Data.url)
        login = LoginPages(driver_setup)
        login.login(Data.valid_username, Data.valid_password)
        sleep(3)
        inventory = InventoryPage(driver_setup)
        inventory.sort_by_value("lohi") # sending the select option value

    def test_reset_app_state(self, driver_setup):
        driver_setup.get(Data.url)
        login = LoginPages(driver_setup)
        login.login(Data.valid_username, Data.valid_password)
        sleep(3)
        inventory = InventoryPage(driver_setup)
        inventory.add_to_cart_by_index(0)
        inventory.reset_app_state() # this will reset all the cart value
        sleep(3)
        cart_text = inventory.find_element(inventory.CART_ICON).text
        # sleep(2)
        assert cart_text == "" # confirm the cart is empty