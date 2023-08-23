from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    """
    BasePage class that provides common methods for interacting with web pages using Selenium WebDriver.
    """

    def __init__(self, browser, url):
        """
        Initialize the BasePage object.
        
        :param browser: An instance of `selenium.webdriver` representing the browser driver.
        :param url: The URL of the current web page.
        """
        self.browser = browser
        self.url = url

    def open(self):
        """
        Open the specified URL in the browser.
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Check if an element is present on the page.
        
        :param how: The method to locate the element (from `selenium.webdriver.common.by`).
        :param what: The unique selector for the element based on the 'how' parameter.
        :return: True if the element is present, False otherwise.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        """
        Check if an element is not present on the page within a specified timeout.
        
        :param how: The method to locate the element (from `selenium.webdriver.common.by`).
        :param what: The unique selector for the element based on the 'how' parameter.
        :param timeout: The maximum time to wait for the element to be absent.
        :return: True if the element is not present, False otherwise.
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, how, what, timeout):
        """
        Check if an element disappears from the page within a specified timeout.
        
        :param how: The method to locate the element (from `selenium.webdriver.common.by`).
        :param what: The unique selector for the element based on the 'how' parameter.
        :param timeout: The maximum time to wait for the element to disappear.
        :return: True if the element disappears, False otherwise.
        """
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def input_text_into_element(self, how, what, input_text, timeout=4):
        """
        Enter text into an input field.
        
        :param how: The method to locate the element (from `selenium.webdriver.common.by`).
        :param what: The unique selector for the element based on the 'how' parameter.
        :param input_text: The text to be entered into the input field.
        :param timeout: The maximum time to wait for the element to be clickable.
        :raises AssertionError: If the input field cannot be filled.
        """
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what))
            )
            element.send_keys(input_text)
        except TimeoutException:
            raise AssertionError(f"Failed to fill the input field of element: {what}")

    def get_text_from_element(self, how, what, timeout=4):
        """
        Get the visible text content from an element.
        
        :param how: The method to locate the element (from `selenium.webdriver.common.by`).
        :param what: The unique selector for the element based on the 'how' parameter.
        :param timeout: The maximum time to wait for the element to be visible.
        :return: The visible text content of the element.
        :raises AssertionError: If the text content cannot be retrieved.
        """
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((how, what))
            )
            text = element.text
        except TimeoutException:
            raise AssertionError(f"Failed to get text attribute from element: {what}")
        return text
    
    def scroll_to_element(self, how, what, timeout=4):
        """
        Scroll the page to bring an element into view.
        
        :param how: The method to locate the element (from `selenium.webdriver.common.by`).
        :param what: The unique selector for the element based on the 'how' parameter.
        :param timeout: The maximum time to wait for the element to be clickable.
        :raises AssertionError: If the element cannot be scrolled into view.
        """
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            raise AssertionError(f"Failed to scroll to element: {what}")
        
    def click_element(self, how, what, timeout=4):
        """
        Scroll to the element and attempt to click it.
        
        :param how: The method used to locate the element. Requires `selenium.webdriver.common.by`.
        :param what: The unique selector of the element, based on the `how` parameter.
        :param timeout: Time in seconds to wait for the element to become clickable.
        :raises AssertionError: If the element is not clickable within the specified timeout.
        """
        try:
            self.scroll_to_element(how, what)
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what))).click()
        except TimeoutException:
            raise AssertionError(f"Failed to click element: {what}")
        
    def double_click_element(self, how, what, timeout=4):
        """
        Scroll to the element and attempt to double click it.
        
        :param how: The method used to locate the element. Requires `selenium.webdriver.common.by`.
        :param what: The unique selector of the element, based on the `how` parameter.
        :param timeout: Time in seconds to wait for the element to become clickable.
        :raises AssertionError: If the element is not clickable within the specified timeout.
        """
        try:
            self.scroll_to_element(how, what)
            button = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
            action = ActionChains(self.browser)
            action.double_click(button).perform()
        except TimeoutException:
            raise AssertionError(f"Failed to double click element: {what}")
        
    def right_click_element(self, how, what, timeout=4):
        """
        Scroll to the element and attempt to right-click it.
        
        :param how: The method used to locate the element. Requires `selenium.webdriver.common.by`.
        :param what: The unique selector of the element, based on the `how` parameter.
        :param timeout: Time in seconds to wait for the element to become clickable.
        :raises AssertionError: If the element is not clickable within the specified timeout.
        """
        try:
            self.scroll_to_element(how, what)
            button = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
            action = ActionChains(self.browser)
            action.context_click(button).perform()
        except TimeoutException:
            raise AssertionError(f"Failed to right click element: {what}")
