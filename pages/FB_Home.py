from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
class FBHome:
   # search="//div[@class='_5861 navigationFocus textInput _5eaz']"
    #search="(//input[@type='text'])[2]"
    search="//input[@class='_5eay']"
    #search="//div[@class='innerWrap']"
    sbtn="//i[@class='_585_']"

    def __init__(self,driver):
        self.driver=driver
        # chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.default_content_setting_values.notifications": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument("start-maximized")


    def find_frnd(self):

        self.driver.find_element_by_xpath(self.search).send_keys("Awantika Pandey Jais")

    def click_search(self):

        self.driver.find_element_by_xpath(self.sbtn).click()

    def search_frnd(self):
        #self.hand_popup()
        self.find_frnd()
        self.click_search()
