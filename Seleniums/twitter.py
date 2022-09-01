from twitterUserinfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time
ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
class Twitter:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome(executable_path='C:/Users/Celal/Documents/pythonProject/Seleniums/chromedriver.exe')
        self.username = username
        self.password = password
    def signIn(self):
        browser=self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        username_in=self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username_in.send_keys(self.username)
        username_in.send_keys(Keys.ENTER)
        time.sleep(2)
        password_in=self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_in.send_keys(self.password)
        password_in.send_keys(Keys.ENTER)
        time.sleep(10)
twt=Twitter(username,password)
twt.signIn()