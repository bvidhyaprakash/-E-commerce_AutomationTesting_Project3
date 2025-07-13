from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class CartPage(BasePage):
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items(self):
        return [element.text for element in self.driver.find_elements(*self.ITEM_NAMES)]