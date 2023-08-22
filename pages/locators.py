from selenium.webdriver.common.by import By

class TextboxPageLocators():
    """Container for unique locators for the `Textbox` page object"""
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

class CheckboxPageLocators():
    """Container for unique locators for the `Checkbox` page object"""
    EXPAND_ALL_BUTTON = (By.CLASS_NAME, "rct-option-expand-all")
    COLLAPSE_ALL_BUTTON = (By.CLASS_NAME, "rct-option-collapse-all")
    HOME_NODE = (By.CSS_SELECTOR, "[for='tree-node-home']")
    DESKTOP_NODE = (By.CSS_SELECTOR, "[for='tree-node-desktop']")
    NOTES_NODE = (By.CSS_SELECTOR, "[for='tree-node-notes']")
    COMMANDS_NODE = (By.CSS_SELECTOR, "[for='tree-node-commands']")
    DOCUMENTS_NODE = (By.CSS_SELECTOR, "[for='tree-node-documents']")
    WORKSPACE_NODE = (By.CSS_SELECTOR, "[for='tree-node-workspace']")
    REACT_NODE = (By.CSS_SELECTOR, "[for='tree-node-react']")
    ANGULAR_NODE = (By.CSS_SELECTOR, "[for='tree-node-angular']")
    VEU_NODE = (By.CSS_SELECTOR, "[for='tree-node-veu']")
    OFFICE_NODE = (By.CSS_SELECTOR, "[for='tree-node-office']")
    PUBLIC_NODE = (By.CSS_SELECTOR, "[for='tree-node-public']")
    PRIVATE_NODE = (By.CSS_SELECTOR, "[for='tree-node-private']")
    CLASSIFIED_NODE = (By.CSS_SELECTOR, "[for='tree-node-classified']")
    GENERAL_NODE = (By.CSS_SELECTOR, "[for='tree-node-general']")
    DOWNLOADS_NODE = (By.CSS_SELECTOR, "[for='tree-node-downloads']")
    WORDFILE_NODE = (By.CSS_SELECTOR, "[for='tree-node-wordFile']")
    EXCELFILE_NODE = (By.CSS_SELECTOR, "[for='tree-node-excelFile']")
    RESULTS = (By.CSS_SELECTOR, "#result .text-success")