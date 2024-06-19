from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument('--user-agent=Selenium')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/ru')

driver.get_cookie('country_code') # словарь
driver.get_cookies() # список словарей

# добавили куку, ниже её вывели
driver.add_cookie({
    'name': 'example',
    'value': 'kukushka'
})

# print(driver.get_cookie('example'))

### Замена куков ###

before = driver.get_cookie('split')
# print(before)
driver.delete_cookie('split')
driver.add_cookie({
    'name': 'split',
    'value': 'qwerty'
})
after = driver.get_cookie('split')
# print(after)

### Удаляем все куки и вставляем только одну куку
driver.delete_all_cookies()

driver.add_cookie({
    'name': 'pechenka',
    'value': 'pecheneg'
})

# print(driver.get_cookie('pechenka'))
# print(driver.get_cookies)





