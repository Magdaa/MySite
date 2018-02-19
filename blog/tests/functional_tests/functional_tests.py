from urllib.parse import urljoin

from selenium import webdriver
import unittest


class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()
        self.browser.implicitly_wait(4)

    def tearDown(self):
        self.browser.quit()

    def test_can_show_main_page_and_find_post(self):
        self.browser.get('http://localhost:8000/blog')
        self.assertIn('Blog', self.browser.title)
        post_titles = self.browser.find_elements_by_tag_name('h3')
        post_titles[0].click()
        post_title_detail=self.browser.find_element_by_tag_name('h3')
        self.assertEqual('Oh lorem oh ipsum', post_title_detail.text)
        self.browser.find_element_by_css_selector('a.btn.btn-default').click()

    def test_can_add_comment(self):
        self.browser.get('http://localhost:8000/blog/oh-lorem-oh-ipsum/comment/')
        author = self.browser.find_element_by_name('author').send_keys('test_user')
        text = self.browser.find_element_by_name('text').send_keys('test_comment')
        self.browser.find_element_by_css_selector('button.save.btn.btn-default')
        self.assertIn('http://localhost:8000/blog/oh-lorem-oh-ipsum/',self.browser.current_url)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
