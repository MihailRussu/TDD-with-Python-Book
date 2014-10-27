from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # open the browser with our ptoject
        self.browser.get('http://localhost:8000')

        # see if the title contains "To-Do"
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # see of the page contains input element

        # try to type something in that input

        # try to hit "Enter" after typing and see if what was typed showed up

        # try to add another item

        # see if the page now has both items

        # try to navigate to one item's url

        # see if the navigated url contains everything

if __name__ == '__main__':
    unittest.main(warnings='ignore')
