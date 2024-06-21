from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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

old_dropdown = 'http://the-internet.herokuapp.com/dropdown'

SELECT_LOCATOR = ('xpath', '//select[@id="dropdown"]')

driver.get(old_dropdown)
time.sleep(1)
DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR)) # Создаём экземпляр класса Select


DROPDOWN.select_by_visible_text('Option 2')
time.sleep(1)
DROPDOWN.select_by_value('1') # У опций есть атрибут value, с помощью него тоже можно выбирать
time.sleep(1)
DROPDOWN.select_by_index(2) # Вроде индексы начинаются с 0, но тут это так не сработало, начались с 1
time.sleep(1)

# Запись данных из Dropdown

ALL_OPTIONS = DROPDOWN.options
# print(ALL_OPTIONS)

# Перебор по тексту
for option in ALL_OPTIONS:
    time.sleep(1)
    if 'Option 1' in option.text:
        print('Опция присутствует')
    # DROPDOWN.select_by_visible_text(option.text)

# Перебор по индексу
for option in ALL_OPTIONS:
    time.sleep(1)
    DROPDOWN.select_by_index(ALL_OPTIONS.index(option))

# Перебор по значению
for option in ALL_OPTIONS:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute('value'))