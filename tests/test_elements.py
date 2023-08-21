import pytest
from pages.textbox_page import TextboxPage

@pytest.mark.textbox_page
class TestTextboxPage():
    """Testing the textbox page via link https://demoqa.com/text-box"""
    link = "https://demoqa.com/text-box"
    name = "John Snow"
    email = "example@fakemail.com"
    current_address = "Some str, 1, 123 apt"
    permanent_address = "Another str, 2, 321 apt"

    @pytest.mark.smoke
    def test_user_can_access_textbox_page(self, browser):
        """
        Simple get to the page
        :param browser: an example of selenium.webdriver
        """
        page = TextboxPage(browser, self.link)
        page.open()
        page.should_be_textbox_page()

    def test_user_can_fill_the_form(self, browser):
        """
        Fill all the fields with correct data, click 'submit' and check if output matches input
        :param browser: an example of selenium.webdriver
        """
        page = TextboxPage(browser, self.link)
        page.open()
        page.should_be_textbox_page()
        page.fill_fullname(self.name)
        page.fill_email(self.email)
        page.fill_current_address(self.current_address)
        page.fill_permanent_address(self.permanent_address)
        page.submit()
        page.should_be_correct_name(self.name)
        page.should_be_correct_email(self.email)
        page.should_be_correct_current_address(self.current_address)
        page.should_be_correct_permanent_address(self.permanent_address)
