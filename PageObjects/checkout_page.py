from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRM_MSG = (By.CLASS_NAME, "complete-header")

    def perform_checkout(self, fname, lname, postal):
        self.click(self.CHECKOUT_BTN)
        self.enter_text(self.FIRST_NAME, fname)
        self.enter_text(self.LAST_NAME, lname)
        self.enter_text(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BTN)
        self.click(self.FINISH_BTN)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRM_MSG)
