from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
chrome_options.add_argument('--ignore-certificate-errors')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 15, poll_frequency=1)


driver.get("https://the-internet.herokuapp.com/dynamic_controls")

ENABLE_BUTTON = ('xpath', '//button[text()="Enable"]')
TEXT_FIELD = ('xpath', '//input[@type="text"]')

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys('Hello')
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, 'Hello'))

print('Vse ok')