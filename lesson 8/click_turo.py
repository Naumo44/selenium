from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get('https://www.freeconferencecall.com/ru/ru')

login_button = driver.find_element('xpath', "//a[@id='login-desktop']")
login_button.click()

email_field = driver.find_element('xpath', "//input[@id='login_email']")
email_field.send_keys('Zeka.2014.ru@gmail.com')

# print(email_field.get_attribute("value"))
email_field.clear()

time.sleep(3)