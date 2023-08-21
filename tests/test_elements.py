import pytest
from pages.textbox_page import TextboxPage

class TestTextboxPage():
    link = "https://demoqa.com/text-box"
    @pytest.mark.smoke
    def test_user_can_access_textbox_page(self, browser):
        page = TextboxPage(browser, self.link)
        page.open()
        page.should_be_textbox_page()