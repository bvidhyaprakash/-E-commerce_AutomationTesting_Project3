from selenium.webdriver.common.by import By
class LocatorDDT:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGOUT_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    username_locator = "user-name"
    password_locator = "password"
    login_button_locator = "login-button"
    profile_dropdown_locator = "react-burger-menu-btn"
    logout_locator = "logout_sidebar_link"