from .base_page import BasePage
from .locators import ButtonsPageLocators

class ButtonsPage(BasePage):
    """
    The page object for `buttons` page in the `elements` section.\n
    This is the child class that extends `BasePage`.
    """
    def should_be_buttons_page(self):
        """Check if the page is really `ButtonsPage`"""
        self.should_be_double_click_button()
        self.should_be_right_click_button()
        self.should_be_left_click_button()
        
    def should_be_double_click_button(self):
        """Check if the `double_click` button is present"""
        assert self.is_element_present(*ButtonsPageLocators.DOUBLE_CLICK_BUTTON), "There is no double_click button!"

    def should_be_right_click_button(self):
        """Check if the `right_click` button is present"""
        assert self.is_element_present(*ButtonsPageLocators.RIGHT_CLICK_BUTTON), "There is no right_click button!"

    def should_be_left_click_button(self):
        """Check if the `left_click` button is present"""
        assert self.is_element_present(*ButtonsPageLocators.LEFT_CLICK_BUTTON), "There is no left_click button!"

    def should_be_double_click_message(self):
        """Check if the `double_click` message is present"""
        assert self.is_element_present(*ButtonsPageLocators.DOUBLE_CLICK_MESSAGE), "There is no double_click message!"

    def should_be_right_click_message(self):
        """Check if the `right_click` message is present"""
        assert self.is_element_present(*ButtonsPageLocators.RIGHT_CLICK_MESSAGE), "There is no right_click message!"

    def should_be_left_click_message(self):
        """Check if the `left_click` message is present"""
        assert self.is_element_present(*ButtonsPageLocators.LEFT_CLICK_MESSAGE), "There is no left_click message!"

    def use_double_click_button(self):
        """Try to use the `double_click` button and assert success"""
        self.double_click_element(*ButtonsPageLocators.DOUBLE_CLICK_BUTTON)
        self.should_be_double_click_message()

    def use_right_click_button(self):
        """Try to use the `right_click` button and assert success"""
        self.right_click_element(*ButtonsPageLocators.RIGHT_CLICK_BUTTON)
        self.should_be_right_click_message()

    def use_left_click_button(self):
        """Try to use the `left_click` button and assert success"""
        self.click_element(*ButtonsPageLocators.LEFT_CLICK_BUTTON)
        self.should_be_left_click_message()
