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
# chrome_options.add_argument("--proxy-server={PROXY_SERVER}")
chrome_options.page_load_strategy='eager'
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument('--user-agent=Selenium')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 5, poll_frequency=1)

HYPERSKILL_LINK = 'https://hyperskill.org/'

FOR_BUSINESS_LOCATOR = ('xpath', '//a[text()="For Business"]')
START_FOR_FREE_LOCATOR = ('xpath', '//a[text()="Start for Free"]')

driver.get(HYPERSKILL_LINK)
time.sleep(3)
# новая вкладка нихуя не открывается
driver.find_element(*FOR_BUSINESS_LOCATOR).click()
time.sleep(3)

tabs = driver.window_handles # список всех вкладок и окон (для selenium это одно и то же)
driver.switch_to.window(tabs[0])
# работать работает, новой вкладки правда на этой сайте не открывается
driver.find_element(*START_FOR_FREE_LOCATOR).click()
time.sleep(3)
driver.current_window_handle # дескриптор текущей страницы
driver.switch_to.new_window('tab') # ну вот так можно создать новую вкладку и там уже что-то открыть
driver.get("https://ya.ru")
time.sleep(3)



