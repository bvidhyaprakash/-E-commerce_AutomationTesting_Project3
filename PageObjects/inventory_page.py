from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from time import sleep

class InventoryPage(BasePage):
    LOGOUT_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_ICON = (By.ID, "shopping_cart_container")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    RESET_BTN = (By.ID, "reset_sidebar_link")

    # this will check for the logout button and click once find.
    def logout(self):
        self.is_visible(self.LOGOUT_MENU_BTN)
        self.click(self.LOGOUT_MENU_BTN)
        sleep(2)
        self.is_visible(self.LOGOUT_LINK)
        self.click(self.LOGOUT_LINK)

    def get_inventory_count_text(self):
        return self.get_text(self.CART_ICON)

    # To check that the Cart icon is displayed or not
    def is_cart_icon_displayed(self):
        return self.is_visible(self.CART_ICON)
    # To get the list of all the products
    def get_all_products(self):
        return self.driver.find_elements(*self.PRODUCTS)

    # To add the item to the card by given index value od lidt or products
    def add_to_cart_by_index(self, index):
        add_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        add_buttons[index].click()

    def open_cart(self):
        self.click(self.CART_ICON)

    #  To sort the products by the given select value
    def sort_by_value(self, value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.find_element(self.SORT_DROPDOWN))
        sleep(3)
        select.select_by_value(value)

    #  To reset all the app settings to the default value
    def reset_app_state(self):
        self.click(self.LOGOUT_MENU_BTN)
        self.is_visible(self.RESET_BTN)
        sleep(2)
        self.click(self.RESET_BTN)