from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
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

modern_checkbox = 'https://demoqa.com/selectable'

# Бывает, что чекбокс реализован не через чекбокс, поэтому в каком-то атрибуте меняется значение
driver.get(modern_checkbox)

checkbox_li = ('xpath', '//li[text()="Cras justo odio"]')
before = driver.find_element(*checkbox_li).get_attribute('class')
driver.find_element(*checkbox_li).click()
after = driver.find_element(*checkbox_li).get_attribute('class')
# В классе в середние дописывается слово active
time.sleep(3)
print(before, after, sep='\n')

