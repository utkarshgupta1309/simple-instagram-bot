from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class InstagramBot:
        def __init__(self):
            self.driver = webdriver.Chrome('chromedriver.exe')
            self.driver.get('https://www.instagram.com/garyvee/')
        def post_comment(self):
            post_list = self.driver.find_elements_by_class_name('_2z6nI')
            print(post_list)
if __name__ == '__main__':
    ig_bot = InstagramBot()
