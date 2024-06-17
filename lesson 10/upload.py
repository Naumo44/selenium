from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os 

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
chrome_options.add_argument('--ignore-certificate-errors')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get('https://the-internet.herokuapp.com/upload')
time.sleep(3)
driver.find_element("xpath", "//input[@type='file']").send_keys(fr"{os.getcwd()}\downloads\cover3.jpeg")
time.sleep(3)