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

complicated_checkbox = "https://demoqa.com/checkbox"

driver.get(complicated_checkbox)

# Тут прикол в том, что кликабелен не сам чекбокс, но статус меняется у него самого
checkbox_home_status = ('xpath', '//input[@id="tree-node-home"]')
checkbox_home_action = ('xpath', '//span[@class="rct-checkbox"]')
driver.find_element(*checkbox_home_action).click()
time.sleep(3)
print(driver.find_element(*checkbox_home_status).is_selected())