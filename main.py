from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import random
import time


s = Service('C:/progs/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.set_window_size(1920, 1080)
driver.get('http://217.71.129.139:4072/login.html')

ran = [random.choice('abc123' if i != 5 else 'ABC') for i in range(10)]
logs = ''.join(ran)

print('log/pass: ', logs)

time.sleep(2)
loginhere = driver.find_element_by_id('login')
loginhere.send_keys(logs)

time.sleep(1)
passhere = driver.find_element_by_id('passw')
passhere.send_keys(logs)

time.sleep(1)
driver.execute_script("javascript:reg()")
time.sleep(1)
driver.execute_script("javascript:login()")

#game
print('zashel v igru')
time.sleep(1)
driver.refresh()
time.sleep(2)

button = driver.find_element_by_id('s0')
for i in range(350):
    button.click()
driver.execute_script("javascript:autoclick()")
driver.execute_script("javascript:autoclick()")
driver.execute_script("javascript:superclick()")
driver.execute_script("javascript:superclick()")

for i in range(200):
    button.click()