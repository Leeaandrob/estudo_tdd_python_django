#coding: utf-8
from unittest import TestCase
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:9000')

assert  'To-Do' in browser.title, "Browser Title was " + browser.title

browser.quit()


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retriever_it_later(self):
        self.browser.get('http://localhost:9000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
