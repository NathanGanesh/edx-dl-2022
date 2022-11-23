from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = 'https://stackoverflow.com/'
path = 'test/scrape.png'
options = webdriver.ChromeOptions()

# options.add_argument('--headless')
options.add_argument('--start-maximized')

prefs = {
    "download.default_directory": "",
    "directory_upgrade": True
}



URL = 'https://learning.edx.org/course/course-v1:MITx+15.415.1x+3T2022/block-v1:MITx+15.415.1x+3T2022+type@sequential+block@3de881daa7bd4cd49fad4259f59874f0/block-v1:MITx+15.415.1x+3T2022+type@vertical+block@94d0701b2b6446dcbeda2148664e3fd9'

options = webdriver.ChromeOptions()
options.headless = False

driver = webdriver.Chrome(service=Service("./bin/chromedriver"), options=options)
driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element_by_tag_name('body').screenshot('web_screenshot2.png')

driver.quit()