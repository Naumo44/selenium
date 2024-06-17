from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--inkognito')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get('https://whatismyipaddress.com/')
time.sleep(3)