from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url='https://www.wikipedia.org/')

url = driver.current_url
print(f'{url=}')
assert url == 'https://www.wikipedia.org/', 'Неверный URL'
title = driver.title
print(f'{title=}')
assert title == 'Wikipedia', 'Неверный заголовок страницы'

time.sleep(3)



