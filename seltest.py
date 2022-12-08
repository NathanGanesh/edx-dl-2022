from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Screenshot import Screenshot
#
# url = 'https://stackoverflow.com/'
# path = 'test/scrape.png'
options = webdriver.ChromeOptions()

# options.add_argument('--headless')
options.add_argument('--start-maximized')
#
# prefs = {
#     "download.default_directory": "",
#     "directory_upgrade": True
# }
#
#
#
# URL = 'http://www.w3schools.com/js/default.asp'
#
options = webdriver.ChromeOptions()
options.headless = False
#
driver = webdriver.Chrome(service=Service("./bin/chromedriver"), options=options)
# driver.get(URL)
# ob = Screenshot_Clipping.Screenshot()
# img = ob.full_Screenshot(driver, save_path=r'D:/OneDrive -Libin/Python/Sel_python/Pytest/Screenshots',
#                          image_name="Screenshot1.png")
#
# driver.quit()



ob = Screenshot.Screenshot()
# driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()