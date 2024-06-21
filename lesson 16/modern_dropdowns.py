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

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy='eager'
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument('--user-agent=Selenium')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 5, poll_frequency=1)

MODERN_DROPDOWNS = 'https://demoqa.com/select-menu'

SELECT_LOCATOR = ('xpath', '//input[@id="react-select-3-input"]')
# этот эелемент не находится, другие не интерактивны, короче нужно искать интерактивный
# всё там есть, ебло ушастое, подождать нужно было побольше, либо использовать явное ожидание
driver.get(MODERN_DROPDOWNS)
time.sleep(3)
driver.find_element(*SELECT_LOCATOR).send_keys('Ms.') # Современные селекты часто реализованы через input
# Так у нас получится найти элемент, чтобы выбрать его, нужно нажать enter
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(1)

SELECT_ONE_LOCATOR = ('xpath', '//div[@id="selectOne"]')
PROF_OPTION = ('xpath', '//div[text()="Prof."]')
# это вот как раз другой способ, нужен, насколько я понял, именно для того, чтобы не было той ошибки, которая была выше
driver.find_element(*SELECT_ONE_LOCATOR).click()
driver.find_element(*PROF_OPTION).click()

