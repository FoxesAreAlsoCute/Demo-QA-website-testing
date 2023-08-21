from .base_page import BasePage
from .locators import TextboxPageLocators

class TextboxPage(BasePage):
    def should_be_textbox_page(self):
        self.should_be_fullname_field()
        self.should_be_email_field()
        self.should_be_current_address_field()
        self.should_be_permanent_address_field()
        self.should_be_submit_button()

    def should_be_fullname_field(self):
        assert self.is_element_present(*TextboxPageLocators.FULL_NAME), "Full name field is not present!"

    def should_be_email_field(self):
        assert self.is_element_present(*TextboxPageLocators.EMAIL), "Email field is not present!"

    def should_be_current_address_field(self):
        assert self.is_element_present(*TextboxPageLocators.CURRENT_ADDRESS), "Current address field is not present!"

    def should_be_permanent_address_field(self):
        assert self.is_element_present(*TextboxPageLocators.PERMANENT_ADDRESS), "Permanent address field is not present!"

    def should_be_submit_button(self):
        assert self.is_element_present(*TextboxPageLocators.SUBMIT_BUTTON), "Submit button is not present!"