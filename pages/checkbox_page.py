from .base_page import BasePage
from .locators import CheckboxPageLocators

class CheckboxPage(BasePage):
    def should_be_checkbox_page(self):
        self.should_be_expand_all_button()
        self.should_be_collapse_all_button()
        self.should_be_home_node()

    def should_be_expand_all_button(self):
        assert self.is_element_present(*CheckboxPageLocators.EXPAND_ALL_BUTTON), "There is no expand all button!"

    def should_be_collapse_all_button(self):
        assert self.is_element_present(*CheckboxPageLocators.COLLAPSE_ALL_BUTTON), "There is no collapse all button!"

    def should_be_all_nodes(self):
        self.should_be_home_node()
        self.should_be_all_nodes_in_home_node()
        self.should_be_all_nodes_in_desktop_node()
        self.should_be_all_nodes_in_documents_node()
        self.should_be_all_nodes_in_workspace_node()
        self.should_be_all_nodes_in_office_node()
        self.should_be_all_nodes_in_downloads_node()

    def should_be_home_node(self):
        assert self.is_element_present(*CheckboxPageLocators.HOME_NODE), "There is no home node!"

    def should_be_all_nodes_in_home_node(self):
        self.should_be_desktop_node()
        self.should_be_documents_node()
        self.should_be_downloads_node()

    def should_be_desktop_node(self):
        assert self.is_element_present(*CheckboxPageLocators.DESKTOP_NODE), "There is no desktop node!"

    def should_be_all_nodes_in_desktop_node(self):
        self.should_be_notes_node()
        self.should_be_commands_node()

    def should_be_notes_node(self):
        assert self.is_element_present(*CheckboxPageLocators.NOTES_NODE), "There is not notes node!"

    def should_be_commands_node(self):
        assert self.is_element_present(*CheckboxPageLocators.COMMANDS_NODE), "There is no commands node!"
    
    def should_be_documents_node(self):
        assert self.is_element_present(*CheckboxPageLocators.DOCUMENTS_NODE), "There is no documents node!"

    def should_be_all_nodes_in_documents_node(self):
        self.should_be_workspace_node()
        self.should_be_office_node()

    def should_be_workspace_node(self):
        assert self.is_element_present(*CheckboxPageLocators.WORKSPACE_NODE), "There is no wowrkspace node!"

    def should_be_all_nodes_in_workspace_node(self):
        self.should_be_react_node()
        self.should_be_angular_node()
        self.should_be_veu_node()

    def should_be_react_node(self):
        assert self.is_element_present(*CheckboxPageLocators.REACT_NODE), "There is no react node!"

    def should_be_angular_node(self):
        assert self.is_element_present(*CheckboxPageLocators.ANGULAR_NODE), "There is no angular node!"

    def should_be_veu_node(self):
        assert self.is_element_present(*CheckboxPageLocators.VEU_NODE), "There is no veu node!"

    def should_be_office_node(self):
        assert self.is_element_present(*CheckboxPageLocators.OFFICE_NODE), "There is no office node!"

    def should_be_all_nodes_in_office_node(self):
        self.should_be_public_node()
        self.should_be_private_node()
        self.should_be_classified_node()
        self.should_be_general_node()

    def should_be_public_node(self):
        assert self.is_element_present(*CheckboxPageLocators.PUBLIC_NODE), "There is no public node!"

    def should_be_private_node(self):
        assert self.is_element_present(*CheckboxPageLocators.PRIVATE_NODE), "There is no private node!"

    def should_be_classified_node(self):
        assert self.is_element_present(*CheckboxPageLocators.CLASSIFIED_NODE), "There is no classified node!"

    def should_be_general_node(self):
        assert self.is_element_present(*CheckboxPageLocators.GENERAL_NODE), "There is no general node!"

    def should_be_downloads_node(self):
        assert self.is_element_present(*CheckboxPageLocators.DOWNLOADS_NODE), "There is no downloads node!"

    def should_be_all_nodes_in_downloads_node(self):
        self.should_be_wordfile_node()
        self.should_be_excelfile_node()

    def should_be_wordfile_node(self):
        assert self.is_element_present(*CheckboxPageLocators.WORDFILE_NODE), "There is no wordfile node!"
    
    def should_be_excelfile_node(self):
        assert self.is_element_present(*CheckboxPageLocators.EXCELFILE_NODE), "There is no excenfile node!"

    def click_expand_all_button(self):
        self.click_element(*CheckboxPageLocators.EXPAND_ALL_BUTTON)

    def click_collapse_all_button(self):
        self.click_element(*CheckboxPageLocators.COLLAPSE_ALL_BUTTON)

    def select_all_nodes(self):
        self.click_element(*CheckboxPageLocators.HOME_NODE)