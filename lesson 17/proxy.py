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

PROXY_SERVER = 'username:passwrod@147.45.104.252:80'# логин и пароль нужен тогда, когда у прокси есть авторизация

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={PROXY_SERVER}")
chrome_options.page_load_strategy='eager'
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument('--user-agent=Selenium')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://2ip.ru/') # 185.140.162.28
time.sleep(5)