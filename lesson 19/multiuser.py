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

HYPERSKILL_URL = 'https://hyperskill.org/login'

LOGIN_FIELD = ('xpath', '//input[@type="email"]')
PASSWORD_FIELD = ('xpath', '//input[@type="password"]')
SUBMIT_BUTTON = ('xpath', '//button[@type="submit"]')

driver.get(HYPERSKILL_URL)
wait.until(EC.visibility_of_element_located(LOGIN_FIELD)).send_keys('alekseik@ya.ru')
driver.find_element(*PASSWORD_FIELD).send_keys('Qwerty132!')
driver.find_element(*SUBMIT_BUTTON).click()
time.sleep(5)

# driver.switch_to.new_window('window')
# driver.get(HYPERSKILL_URL) # если просто открыть ссылку в новой вкладке, то авторизация сохранится
# time.sleep(3)

# для того, чтобы создать новую сессию, нужно создать новый экземпляр драйвера, новая вкладка вообще не понадобится

user_2 = webdriver.Chrome(options=chrome_options, service=service)

user_2.get(HYPERSKILL_URL)
time.sleep(5)