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

driver.get('https://www.freeconferencecall.com/ru')

# тут нужно сначала залогиниться

pickle.dump(driver.get_cookies(), open(os.getcwd()+'/cookies/cookies.pkl', 'wb'))

cookies = pickle.load(open(os.getcwd()+'/cookies/cookies.pkl', 'rb'))
# print(cookies)
driver.delete_all_cookies()
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(5)
driver.refresh()
time.sleep(5)
'''
В чём тут вообще смысл: мы залогинились, сохранили куки, в них есть авторизационные данные
если вставить авторизационные куки, то мы автоматически залогинимся после обновления страницы.
Мы залогинились, сохранили куки, после этого мы можем удалить все куки, вставить свои,
перезагрузить страницу и, соответственно, залогиниться
'''
