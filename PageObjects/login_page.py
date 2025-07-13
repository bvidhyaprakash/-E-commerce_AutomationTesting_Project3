from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class LoginPages(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")


    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(LoginPages)

    def is_login_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)