from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class InventoryPage(BasePage):
    LOGOUT_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_ICON = (By.ID, "shopping_cart_container")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    RESET_BTN = (By.ID, "reset_sidebar_link")

    def logout(self):
        self.click(self.LOGOUT_MENU_BTN)
        self.click(self.LOGOUT_LINK)