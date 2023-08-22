from .base_page import BasePage
from .locators import CheckboxPageLocators

class CheckboxPage(BasePage):
    """
    The page object for checkbox page in the `elements` section.\n
    This is the child class that extends `BasePage`.
    """
    def should_be_checkbox_page(self):
        """Check if the page is really `CheckboxPage`"""
        self.should_be_expand_all_button()
        self.should_be_collapse_all_button()
        self.should_be_home_node()

    def should_be_expand_all_button(self):
        """Check if `EXPAND ALL` button is present"""
        assert self.is_element_present(*CheckboxPageLocators.EXPAND_ALL_BUTTON), "There is no expand all button!"

    def should_be_collapse_all_button(self):
        """Check if `COLLAPSE ALL` button is present"""
        assert self.is_element_present(*CheckboxPageLocators.COLLAPSE_ALL_BUTTON), "There is no collapse all button!"

    def should_be_all_nodes(self):
        """Check if all nodes are visible"""
        self.should_be_home_node()
        self.should_be_all_nodes_in_home_node()
        self.should_be_all_nodes_in_desktop_node()
        self.should_be_all_nodes_in_documents_node()
        self.should_be_all_nodes_in_workspace_node()
        self.should_be_all_nodes_in_office_node()
        self.should_be_all_nodes_in_downloads_node()

    def should_be_home_node(self):
        """Check visiblity of `home` node"""
        assert self.is_element_present(*CheckboxPageLocators.HOME_NODE), "There is no home node!"

    def should_be_all_nodes_in_home_node(self):
        """Check visiblity of all nodes under `home`"""
        self.should_be_desktop_node()
        self.should_be_documents_node()
        self.should_be_downloads_node()

    def should_be_desktop_node(self):
        """Check visiblity of `desktop` node"""
        assert self.is_element_present(*CheckboxPageLocators.DESKTOP_NODE), "There is no desktop node!"

    def should_be_all_nodes_in_desktop_node(self):
        """Check visiblity of all nodes under `desktop`"""
        self.should_be_notes_node()
        self.should_be_commands_node()

    def should_be_notes_node(self):
        """Check visiblity of `notes` node"""
        assert self.is_element_present(*CheckboxPageLocators.NOTES_NODE), "There is not notes node!"

    def should_be_commands_node(self):
        """Check visiblity of `commands` node"""
        assert self.is_element_present(*CheckboxPageLocators.COMMANDS_NODE), "There is no commands node!"
    
    def should_be_documents_node(self):
        """Check visiblity of `documents` node"""
        assert self.is_element_present(*CheckboxPageLocators.DOCUMENTS_NODE), "There is no documents node!"

    def should_be_all_nodes_in_documents_node(self):
        """Check visiblity of all nodes under `documents`"""
        self.should_be_workspace_node()
        self.should_be_office_node()

    def should_be_workspace_node(self):
        """Check visiblity of `workspace` node"""
        assert self.is_element_present(*CheckboxPageLocators.WORKSPACE_NODE), "There is no wowrkspace node!"

    def should_be_all_nodes_in_workspace_node(self):
        """Check visiblity of all nodes under `workspace`"""
        self.should_be_react_node()
        self.should_be_angular_node()
        self.should_be_veu_node()

    def should_be_react_node(self):
        """Check visiblity of `react` node"""
        assert self.is_element_present(*CheckboxPageLocators.REACT_NODE), "There is no react node!"

    def should_be_angular_node(self):
        """Check visiblity of `angular` node"""
        assert self.is_element_present(*CheckboxPageLocators.ANGULAR_NODE), "There is no angular node!"

    def should_be_veu_node(self):
        """Check visiblity of `veu` node"""
        assert self.is_element_present(*CheckboxPageLocators.VEU_NODE), "There is no veu node!"

    def should_be_office_node(self):
        """Check visiblity of `office` node"""
        assert self.is_element_present(*CheckboxPageLocators.OFFICE_NODE), "There is no office node!"

    def should_be_all_nodes_in_office_node(self):
        """Check visiblity of all nodes under `office`"""
        self.should_be_public_node()
        self.should_be_private_node()
        self.should_be_classified_node()
        self.should_be_general_node()

    def should_be_public_node(self):
        """Check visiblity of `public` node"""
        assert self.is_element_present(*CheckboxPageLocators.PUBLIC_NODE), "There is no public node!"

    def should_be_private_node(self):
        """Check visiblity of `private` node"""
        assert self.is_element_present(*CheckboxPageLocators.PRIVATE_NODE), "There is no private node!"

    def should_be_classified_node(self):
        """Check visiblity of `classified` node"""
        assert self.is_element_present(*CheckboxPageLocators.CLASSIFIED_NODE), "There is no classified node!"

    def should_be_general_node(self):
        """Check visiblity of `general` node"""
        assert self.is_element_present(*CheckboxPageLocators.GENERAL_NODE), "There is no general node!"

    def should_be_downloads_node(self):
        """Check visiblity of `downloads` node"""
        assert self.is_element_present(*CheckboxPageLocators.DOWNLOADS_NODE), "There is no downloads node!"

    def should_be_all_nodes_in_downloads_node(self):
        """Check visiblity of all nodes under `downloads`"""
        self.should_be_wordfile_node()
        self.should_be_excelfile_node()

    def should_be_wordfile_node(self):
        """Check visiblity of `wordfile` node"""
        assert self.is_element_present(*CheckboxPageLocators.WORDFILE_NODE), "There is no wordfile node!"
    
    def should_be_excelfile_node(self):
        """Check visiblity of `excelfile` node"""
        assert self.is_element_present(*CheckboxPageLocators.EXCELFILE_NODE), "There is no excenfile node!"


    def click_expand_all_button(self):
        """Click a button to expand the whole dropdown"""
        self.click_element(*CheckboxPageLocators.EXPAND_ALL_BUTTON)

    def click_collapse_all_button(self):
        """Click a button to collapse the dropdown completely"""
        self.click_element(*CheckboxPageLocators.COLLAPSE_ALL_BUTTON)


    def select_all_nodes(self):
        """Select all nodes by clicking on `home` node"""
        self.click_element(*CheckboxPageLocators.HOME_NODE)

    def expected_text_present_in_results_array(self, expected_text):
        """
        Check if some text `expected_text` is present in `results` array
        :param expected_text: Some text that is expected to be seen in the `results`
        """
        arr = self.browser.find_elements(*CheckboxPageLocators.RESULTS)
        if len(arr) == 0:
            raise AssertionError (f"There is no any {CheckboxPageLocators.RESULTS}!")
        for i in arr:
            if i.text == expected_text:
                return
        raise AssertionError(f"There is no '{expected_text}' in results!")
    
    def should_be_all_results(self):
        """Check if all possible results are present"""
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
        """Check if `home` is present in results"""
        self.expected_text_present_in_results_array("home")

    def should_be_desktop_in_results(self):
        """Check if `desctop` is present in results"""
        self.expected_text_present_in_results_array("desktop")
    
    def should_be_notes_in_results(self):
        """Check if `notes` is present in results"""
        self.expected_text_present_in_results_array("notes")

    def should_be_commands_in_results(self):
        """Check if `commnds` is present in results"""
        self.expected_text_present_in_results_array("commands")
        
    def should_be_documents_in_results(self):
        """Check if `documents` is present in results"""
        self.expected_text_present_in_results_array("documents")

    def should_be_workspace_in_results(self):
        """Check if `workspace` is present in results"""
        self.expected_text_present_in_results_array("workspace")

    def should_be_react_in_results(self):
        """Check if `react` is present in results"""
        self.expected_text_present_in_results_array("react")

    def should_be_angular_in_results(self):
        """Check if `angular` is present in results"""
        self.expected_text_present_in_results_array("angular")

    def should_be_veu_in_results(self):
        """Check if `veu` is present in results"""
        self.expected_text_present_in_results_array("veu")

    def should_be_office_in_results(self):
        """Check if `office` is present in results"""
        self.expected_text_present_in_results_array("office")

    def should_be_public_in_results(self):
        """Check if `public` is present in results"""
        self.expected_text_present_in_results_array("public")

    def should_be_private_in_results(self):
        """Check if `private` is present in results"""
        self.expected_text_present_in_results_array("private")

    def should_be_classified_in_results(self):
        """Check if `classified` is present in results"""
        self.expected_text_present_in_results_array("classified")

    def should_be_general_in_results(self):
        """Check if `general` is present in results"""
        self.expected_text_present_in_results_array("general")

    def should_be_downloads_in_results(self):
        """Check if `downloads` is present in results"""
        self.expected_text_present_in_results_array("downloads")

    def should_be_wordfile_in_results(self):
        """Check if `wordFile` is present in results"""
        self.expected_text_present_in_results_array("wordFile")

    def should_be_excelfile_in_results(self):
        """Check if `excelFile` is present in results"""
        self.expected_text_present_in_results_array("excelFile")
