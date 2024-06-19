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

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ('xpath', '//button[@id="visibleAfter"]')

# ждёт, пока элемент появится или станет видимым
BUTTON = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
BUTTON.click()

# ждёт, пока кнопка станет кликабельной
ENABLE_IN_SECONDS = ('xpath', '//button[@id="visibleAfter"')
wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS)).click()


