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

driver.get('https://demoqa.com/alerts')

BUTTON_2 = ('xpath', '//button[@id="confirmButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_2)).click()

alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
print(alert.text)
alert.dismiss()
time.sleep(3)