import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
chrome_options.add_argument('--ignore-certificate-errors')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 5, poll_frequency=1)

SITE_URL = 'https://testautomationpractice.blogspot.com/'
FROM_NAME_FIELD_LOCATOR = ('xpath', '//input[@id="RESULT_TextField-0"]')

driver.get(SITE_URL)
wait.until(EC.visibility_of_element_located(FROM_NAME_FIELD_LOCATOR)).send_keys('Eugene')
time.sleep(3)