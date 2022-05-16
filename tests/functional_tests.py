import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_homepage(self):
        # Shingi has heard about a blog being run by one of her friends
        # from her workplace. She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention book boardroom
        self.assertIn("Anna Makarudze", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Blog", header_text)

        # She visits another page
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
