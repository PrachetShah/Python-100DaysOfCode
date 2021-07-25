from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = YOURCHROMEDRIVERPATH
INSTA_USER = ACC_USER
INSTA_PASS = ACC_PASS
SEARCH_ACC = ACCOUNT_YOU_WANT_TO_SEARCH


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        time.sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(INSTA_USER)

        time.sleep(2)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASS)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        not_save = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_save.send_keys(Keys.ENTER)

        time.sleep(2)
        no_noti = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        no_noti.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(1)
        search_acc = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_acc.send_keys(SEARCH_ACC)

        time.sleep(2)
        search_acc.send_keys(Keys.ENTER)
        time.sleep(0.5)
        search_acc.send_keys(Keys.ENTER)

        time.sleep(1)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        followers.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                time.sleep(1)
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
