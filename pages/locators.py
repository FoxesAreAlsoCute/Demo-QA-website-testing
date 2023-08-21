from selenium.webdriver.common.by import By

class TextboxPageLocators():
    """Container for unique locators for the Textbox page object"""
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    CHECK_NAME = (By.CSS_SELECTOR, "p#name")
    CHECK_EMAIL = (By.CSS_SELECTOR, "p#email")
    CHECK_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p#currentAddress")
    CHECK_PERMANENT_ADDRESS = (By. CSS_SELECTOR, "p#permanentAddress")
    INCORRECT_LOCATOR = (By.CSS_SELECTOR, "INCORRECT_LOCATOR") # For sure that tests work