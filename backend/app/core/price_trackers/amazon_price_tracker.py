import aiohttp
import asyncio
from bs4 import BeautifulSoup
from base_price_tracker import BasePriceTracker


class AmazonPriceTracker(BasePriceTracker):
    def __init__(self, *args, **kwargs):
        super(AmazonPriceTracker, self).__init__(*args, **kwargs)
        
    def get_price(self, url):
        html = self.get(url)
        dom = BeautifulSoup(html, 'html.parser')
        return dom.select_one('#priceblock_ourprice').text
#launch url
#url = 'https://www.amazon.com/gp/product/B01HOS31B0?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=VJQJJSGTMRT23K2K6S8T'
"""
# create a new Firefox session
options = Options()
options.add_argument('--ignore-certificate-errors')
#options.binary_location = "bin/chrome77_win/chrome.exe"

driver = webdriver.Chrome(chrome_options=options, executable_path="bin/chromedriver.exe")
#driver.implicitly_wait(1)
driver.get(url);
html = driver.page_source
print(html)
"""
if __name__ == "__main__":
    url = 'https://www.amazon.com/gp/product/B01HOS31B0?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=VJQJJSGTMRT23K2K6S8T'
    source = AmazonPriceTracker().get_price(url)
    print(source)