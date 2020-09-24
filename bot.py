from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



class InstagramBot:
    def __init__(self,username,password):
        self.username =username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.base_url = 'https://www.instagram.com'
        self.login()

    def login(self):
        self.driver.get('{}/accounts/login'.format(self.base_url))
        enter_username = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

    def follow_user(self,user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]
        follow_button.click()
    def unfollow_user(self,user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(),'Following')]")[0]
        follow_button.click()

    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))

    def open_post(self):
        open_post1 = self.driver.find_element_by_tag_name('a')[0]
        open_post1.click()
        # open_post.click()


if __name__ == '__main__':
    ig_bot = InstagramBot('gsushwg@gmail.com','Thisisabot69')
    time.sleep(3)
    ig_bot.nav_user('garyvee')
    # ig_bot = InstagramBot('1111111','11111111111')
    # ig_bot.follow_user('spellbathing')
    ig_bot.open_post()
