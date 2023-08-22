from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class BasePage():
    """The page object with most common methods on each other page of the project"""
    def __init__(self, browser, url):
        """
        Initialize the page object
        :param browser: example of selenium.webdriver
        :param url: the link of the current page object
        """
        self.browser = browser
        self.url = url

    def open(self):
        """Open url in opened browser"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Check if element is present on the page
        :param how: requires 'selenium.webdriver.common.by'
        :param what: the unique selector on the element, depends on 'how' parameter
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        """
        Check if element is not present on the page
        :param how: requires 'selenium.webdriver.common.by'
        :param what: the unique selector on the element, depends on 'how' parameter
        :param timeout: time to try and find the element on the page
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_dissapeared(self, how, what, timeout):
        """
        Check if element is not present on the page any more after some seconds
        :param how: requires 'selenium.webdriver.common.by'
        :param what: the unique selector on the element, depends on 'how' parameter
        :param timeout: time to try and find the element on the page
        """
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def input_text_into_element(self, how, what, inputtext, timeout=4):
        """
        Try to fill an input field
        :param how: requires 'selenium.webdriver.common.by'
        :param what: the unique selector on the element, depends on 'how' parameter
        :param inputtext: the text which must be filled in the input field
        :param timeout: time to try and assure that the element is clickable
        :raises AssertionError:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what))).send_keys(inputtext)
        except TimeoutException:
            raise AssertionError(f"Failed to fill the input field of element: {what}")

    def get_text_from_element(self, how, what, timeout=4):
        """
        Try to get the value of 'text' property
        :param how: requires 'selenium.webdriver.common.by'
        :param what: the unique selector on the element, depends on 'how' parameter
        :param timeout: time to try and assure that the element is clickable
        :return: string
        :raises AssertionError:
        """
        try:
            text = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what))).text
        except TimeoutException:
            raise AssertionError(f"Failed to get text attribute from element: {what}")
        return text
    
    def scroll_to_element(self, how, what, timeout=4):
        """
        Try to scroll to element
        :param how: requires 'selenium.webdriver.common.by'
        :param what: the unique selector on the element, depends on 'how' parameter
        :param timeout: time to try and assure that the element is clickable
        :raises AssertionError:
        """
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            raise AssertionError(f"Failed to scroll to element {what}")
        
    def click_element(self, how, what, timeout=4):
        """
        Try to click the element, but at first scroll to it
        :param how: requires 'selenium.webdriver.common.by'
        :param what: the unique selector on the element, depends on 'how' parameter
        :param timeout: time to try and assure that the element is clickable
        :raises AssertionError:
        """
        try:
            self.scroll_to_element(how, what)
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what))).click()
        except TimeoutException:
            raise AssertionError(f"Failed to click element: {what}")
