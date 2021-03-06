from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_for_one_user(self):
        # Jon has heard about a cool new online to-do app.  She goes to check out its homepage.
        self.browser.get(self.get_server_url())
        # He notices that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Eat an entire chair" into a text box
        inputbox.send_keys('Eat an entire chair')

        # When he hits enter, the page updates, and now the page lists:
        # "1: Eat an entire chair" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Eat an entire chair')

        # There is still a text box inviting him to add another item.  He enters "Collapse into nothing"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Collapse into nothing')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Eat an entire chair')
        self.wait_for_row_in_list_table('2: Collapse into nothing')

        # He collapses into nothing

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Jon starts a new to-do list
        self.browser.get(self.get_server_url())
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Eat an entire chair')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Eat an entire chair')

        # She notices that her list has a unique URL
        jon_list_url = self.browser.current_url
        self.assertRegex(jon_list_url, '/lists/.+')

        # Now a new user, Gary, comes along to the site.

        ## We use a new browser session to make sure that no information of Jon's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Gary visits the home page. There is no sign of Jon's list
        self.browser.get(self.get_server_url())
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Eat an entire chair', page_text)
        self.assertNotIn('Collapse into nothing', page_text)

        # Gary starts a new list by entering a new item.  He is more traditionally evil.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Pay homage to the byzantine consort')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Pay homage to the byzantine consort')

        # Gary gets his own unique URL
        gary_list_url = self.browser.current_url
        self.assertRegex(gary_list_url, '/lists/.+')
        self.assertNotEqual(gary_list_url, jon_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Eat an entire chair', page_text)
        self.assertIn('Pay homage to the byzantine consort', page_text)

        # Satisfied, they both collapse into nothing