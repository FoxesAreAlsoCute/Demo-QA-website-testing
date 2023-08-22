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

    def expected_text_present_in_results_array(self, expected_text):
        arr = self.browser.find_elements(*CheckboxPageLocators.RESULTS)
        if len(arr) == 0:
            raise AssertionError (f"There is no any {CheckboxPageLocators.RESULTS}!")
        for i in arr:
            if i.text == expected_text:
                return
        raise AssertionError(f"There is no '{expected_text}' in results!")
    
    def should_be_all_results(self):
        self.should_be_home_in_results()
        self.should_be_desktop_in_results()
        self.should_be_notes_in_results()
        self.should_be_commands_in_results()
        self.should_be_documents_in_results()
        self.should_be_workspace_in_results()
        self.should_be_react_in_results()
        self.should_be_angular_in_results()
        self.should_be_veu_in_results()
        self.should_be_office_in_results()
        self.should_be_public_in_results()
        self.should_be_private_in_results()
        self.should_be_classified_in_results()
        self.should_be_general_in_results()
        self.should_be_downloads_in_results()
        self.should_be_wordfile_in_results()
        self.should_be_excelfile_in_results()

    def should_be_home_in_results(self):
        self.expected_text_present_in_results_array("home")

    def should_be_desktop_in_results(self):
        self.expected_text_present_in_results_array("desktop")
    
    def should_be_notes_in_results(self):
        self.expected_text_present_in_results_array("notes")

    def should_be_commands_in_results(self):
        self.expected_text_present_in_results_array("commands")
        
    def should_be_documents_in_results(self):
        self.expected_text_present_in_results_array("documents")

    def should_be_workspace_in_results(self):
        self.expected_text_present_in_results_array("workspace")

    def should_be_react_in_results(self):
        self.expected_text_present_in_results_array("react")

    def should_be_angular_in_results(self):
        self.expected_text_present_in_results_array("angular")

    def should_be_veu_in_results(self):
        self.expected_text_present_in_results_array("veu")

    def should_be_office_in_results(self):
        self.expected_text_present_in_results_array("office")

    def should_be_public_in_results(self):
        self.expected_text_present_in_results_array("public")

    def should_be_private_in_results(self):
        self.expected_text_present_in_results_array("private")

    def should_be_classified_in_results(self):
        self.expected_text_present_in_results_array("classified")

    def should_be_general_in_results(self):
        self.expected_text_present_in_results_array("general")

    def should_be_downloads_in_results(self):
        self.expected_text_present_in_results_array("downloads")

    def should_be_wordfile_in_results(self):
        self.expected_text_present_in_results_array("wordFile")

    def should_be_excelfile_in_results(self):
        self.expected_text_present_in_results_array("excelFile")
