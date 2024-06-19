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

radio_button = 'https://demoqa.com/radio-button'

driver.get(radio_button)

radio_yes_status = ('xpath', '//input[@id="yesRadio"]')
radio_yes_action = ('xpath', '//label[@for="yesRadio"]')
# кнопка no в статусе disabled
radio_no =  ('xpath', '//input[@id="noRadio"]')

# print(driver.find_element(*radio_yes_status).is_selected())
driver.find_element(*radio_yes_action).click()
# print(driver.find_element(*radio_yes_status).is_selected())
time.sleep(3)

print(driver.find_element(*radio_no).is_selected())
