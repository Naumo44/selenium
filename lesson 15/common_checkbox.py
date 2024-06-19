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

common_checkbox = 'http://the-internet.herokuapp.com/checkboxes'
complicated_checkbox = "https://demoqa.com/checkbox"
modern_checkbox = 'https://demoqa.com/selectable'
radio_button = 'https://demoqa.com/radio-button'

# обычные чекбоксы
driver.get(common_checkbox)
checkbox_1 = ('xpath', '//input[@type="checkbox"][1]')
# print(driver.find_element(*checkbox_1).get_attribute('checked'))
print(driver.find_element(*checkbox_1).is_selected())
driver.find_element(*checkbox_1).click()
# print(driver.find_element(*checkbox_1).get_attribute('checked'))
# атрибут возвращает либо None, либо строку, метод же возвращает True/False
print(driver.find_element(*checkbox_1).is_selected()) 
time.sleep(3)

