import pytest
from pages.textbox_page import TextboxPage
from pages.checkbox_page import CheckboxPage

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
        Simple get to the `Textbox` page
        :param browser: an example of `selenium.webdriver`
        """
        page = TextboxPage(browser, self.link)
        page.open()
        page.should_be_textbox_page()

    def test_user_can_fill_the_form(self, browser):
        """
        Fill all the fields with correct data, click `submit` and check if output matches input
        :param browser: an example of `selenium.webdriver`
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


@pytest.mark.checkbox_page
class TestCheckboxPage():
    """Testing the checkbox page via link https://demoqa.com/checkbox"""
    link = "https://demoqa.com/checkbox"

    @pytest.mark.smoke
    def test_user_can_access_checkbox_page(self, browser):
        """
        Simple get to the `Checkbox` page
        :param browser: an example of `selenium.webdriver`
        """
        page = CheckboxPage(browser, self.link)
        page.open()
        page.should_be_checkbox_page()

    def test_user_can_see_all_nodes_after_expand_all(self, browser):
        """
        Check visibility of all elements after expand completely the dropdown
        :param browser: an example of `selenium.webdriver`
        """
        page = CheckboxPage(browser, self.link)
        page.open()
        page.should_be_checkbox_page()
        page.click_expand_all_button()
        page.should_be_all_nodes()

    def test_user_can_select_all_nodes(self, browser):
        """
        Check if all elements are selected after clicking the `home` node
        :param browser: an example of `selenium.webdriver`
        """
        page = CheckboxPage(browser, self.link)
        page.open()
        page.should_be_checkbox_page()
        page.select_all_nodes()
        page.should_be_all_results()