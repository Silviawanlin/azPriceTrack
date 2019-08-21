from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class BasePriceTracker:
    def __init__(self):
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        #options.binary_location = "bin/chrome77_win/chrome.exe"
        self.driver = webdriver.Chrome(chrome_options=options, executable_path="bin/chromedriver.exe")
    def get(self, url):
        self.driver.get(url)
        return self.driver.page_source