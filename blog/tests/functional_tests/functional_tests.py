from selenium import webdriver
import unittest


class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()
        self.browser.implicitly_wait(4)

    def tearDown(self):
        self.browser.quit()

    def test_can_show_main_page_and_go_to_post(self):
        self.browser.get('http://localhost:8000/blog')
        self.assertIn('Blog', self.browser.title)
        post_title = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Photos-photos', post_title)
    #    self.fail('Finish the tests!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
