from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
class FBLogin:
    un = "//input[@id='email']"
    pwd = "//input[@id='pass']"
    lbtn = "//button[@id='u_0_b']"

    def __init__(self, driver):
        self.driver = driver
        #self.url = url

    # def get_url(self):
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()


    def enter_un(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.un).send_keys("sapnakri2811@gmail.com")

    def enter_pwd(self):
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath(self.pwd).send_keys("ihv@1bro")

    def click_login(self):
        self.driver.find_element_by_xpath(self.lbtn).click()

    def login_credentials(self):
        # self.get_url()
        print("in credentials.")
        self.enter_un()
        self.enter_pwd()
        self.click_login()
        print("Logged in")
        #self.hand_popup()
