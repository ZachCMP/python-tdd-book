from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Jon goes to the home page and accidentally tries to submit an empty list item.  He hits enter on the empty input box

        # The home page refreshes, and there is an error message saying that list items cannot be blank

        # He tries again with some text for the item, which now works

        # He now decides to submit a second blank list item

        # He receives a similar warning on the list page

        # He can correct it by filling some text in

        self.fail('Write me')