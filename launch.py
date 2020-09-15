from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.options import Options
driver=webdriver.Chrome(executable_path=r'C:\Users\sapna\PycharmProjects\pythonProject\FBFramework\Drivers\chromedriver.exe')
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://www.facebook.com/")

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("start-maximized")