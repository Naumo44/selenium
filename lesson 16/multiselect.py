from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
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

MODERN_DROPDOWNS = 'https://demoqa.com/select-menu'

MULTISELECT_LOCATOR = ('xpath', '//input[@id="react-select-4-input"]')

driver.get(MODERN_DROPDOWNS)
time.sleep(3)
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Green')
# можно использовать таб для автодозаполнения
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
driver.find_element(*MULTISELECT_LOCATOR).send_keys('Black')
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(3)