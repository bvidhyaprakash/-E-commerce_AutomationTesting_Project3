from selenium.webdriver.support.expected_conditions import element_located_to_be_selected
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
            return web_element
        except(NoSuchElementException, ElementNotVisibleException, TimeoutException) as error:
            print("Error: ", error)

    def find_elements(self, locator):
        try:
            web_elements = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator))
            return web_elements
        except(NoSuchElementException, ElementNotVisibleException, TimeoutException) as error:
            print("Error :", error)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

