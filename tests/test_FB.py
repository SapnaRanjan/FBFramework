import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
from launch import driver
from pages.Fb_Login import FBLogin
from pages.FB_Home import FBHome

class TestFB:

    def test_Login(self):
        obj= ActionChains(driver)
        time.sleep(5)
        lp = FBLogin(driver)
        lp.login_credentials()
        time.sleep(5)
        obj.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        obj.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    def test_Home(self):
        pass
        #hp= FBHome(driver)
       # hp.search_frnd()
