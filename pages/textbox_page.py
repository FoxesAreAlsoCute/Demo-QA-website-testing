from .base_page import BasePage
from .locators import TextboxPageLocators

class TextboxPage(BasePage):
    """
    The page object for textbox page in the 'elements' section.\n
    This is the child class that extends BasePage.
    """
    def should_be_textbox_page(self):
        """Check if the page is really Textbox page"""
        self.should_be_fullname_field()
        self.should_be_email_field()
        self.should_be_current_address_field()
        self.should_be_permanent_address_field()
        self.should_be_submit_button()

    def should_be_fullname_field(self):
        """Check if there is a fullname input field"""
        assert self.is_element_present(*TextboxPageLocators.FULL_NAME), "Full name field is not present!"

    def should_be_email_field(self):
        """Check if there is an email input field"""
        assert self.is_element_present(*TextboxPageLocators.EMAIL), "Email field is not present!"

    def should_be_current_address_field(self):
        """Check if there is a current address input field"""
        assert self.is_element_present(*TextboxPageLocators.CURRENT_ADDRESS), "Current address field is not present!"

    def should_be_permanent_address_field(self):
        """Check if there is a permanent address input field"""
        assert self.is_element_present(*TextboxPageLocators.PERMANENT_ADDRESS), "Permanent address field is not present!"

    def should_be_submit_button(self):
        """Check if there is a submit button"""
        assert self.is_element_present(*TextboxPageLocators.SUBMIT_BUTTON), "Submit button is not present!"

    
    def fill_fullname(self, inputtext):
        """
        Fill the fullname input field
        :param inputtext: the text which will be put into the input field
        """
        self.input_text_into_element(*TextboxPageLocators.FULL_NAME, inputtext)

    def fill_email(self, inputtext):
        """
        Fill the email input field
        :param inputtext: the text which will be put into the input field
        """
        self.input_text_into_element(*TextboxPageLocators.EMAIL, inputtext)

    def fill_current_address(self, inputtext):
        """
        Fill the current address input field
        :param inputtext: the text which will be put into the input field
        """
        self.input_text_into_element(*TextboxPageLocators.CURRENT_ADDRESS, inputtext)
        
    def fill_permanent_address(self, inputtext):
        """
        Fill the permanent address input field
        :param inputtext: the text which will be put into the input field
        """
        self.input_text_into_element(*TextboxPageLocators.PERMANENT_ADDRESS, inputtext)

    def submit(self):
        """Click the submit button"""
        self.click_element(*TextboxPageLocators.SUBMIT_BUTTON)


    def should_be_correct_name(self, inputtext):
        """
        Check if the output name is correct
        :param inputtext: the text which is expected to be in the output field
        """
        required_text = self.get_text_from_element(*TextboxPageLocators.CHECK_NAME)
        assert inputtext in required_text, f"Wrong name! Expected: {inputtext}, receved: {required_text}"

    def should_be_correct_email(self, inputtext):
        """
        Check if the output email is correct
        :param inputtext: the text which is expected to be in the output field
        """
        required_text = self.get_text_from_element(*TextboxPageLocators.CHECK_EMAIL)
        assert inputtext in required_text, f"Wrong email! Expected: {inputtext}, receved: {required_text}"

    def should_be_correct_current_address(self, inputtext):
        """
        Check if the output current address is correct
        :param inputtext: the text which is expected to be in the output field
        """
        required_text = self.get_text_from_element(*TextboxPageLocators.CHECK_CURRENT_ADDRESS)
        assert inputtext in required_text, f"Wrong current address! Expected: {inputtext}, receved: {required_text}"

    def should_be_correct_permanent_address(self, inputtext):
        """
        Check if the output permanent address is correct
        :param inputtext: the text which is expected to be in the output field
        """
        required_text = self.get_text_from_element(*TextboxPageLocators.CHECK_PERMANENT_ADDRESS)
        assert inputtext in required_text, f"Wrong permanent address! Expected: {inputtext}, receved: {required_text}"
