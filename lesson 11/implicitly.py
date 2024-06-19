from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
chrome_options.add_argument('--ignore-certificate-errors')
prefs = {
    'download.default_directory': f'{os.getcwd()}\\downloads'
}
chrome_options.add_experimental_option('prefs', prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ('xpath', r'//button[@id="visibleAfter"]')
driver.find_element(*VISIBLE_AFTER_BUTTON).click()
time.sleep(3)
