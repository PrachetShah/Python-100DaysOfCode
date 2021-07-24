from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 30
PROMISED_UP = 25
CHROME_DRIVER_PATH = CHROME_DRIVER_PATH
TWITTER_USERNAME = USERNAME
TWITTER_PASS = PASSWORD


class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.go = self.driver.find_element_by_css_selector("a .start-text")
        self.go.click()

        time.sleep(45)
        self.download = self.driver.find_element_by_css_selector("div .result-data .download-speed")
        self.download = self.download.text
        self.upload = self.driver.find_element_by_css_selector("div .result-data .upload-speed")
        self.upload = self.upload.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(3)
        username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)

        time.sleep(2)
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed down to {self.download} and upload speed is"
                        f" {self.upload} when i pay for {self.down}mbps/{self.up}mbps ")

        time.sleep(2)
        send_tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        send_tweet.click()


speed = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
speed.get_internet_speed()
speed.tweet_at_provider()




