from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import time

# start timer 
start = time.time()
# counter 
count = 1

# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()

# webdriver 
url = 'https://www.zennichi.or.jp/member_search/'
driver = webdriver.Chrome()
driver.get(url)


# prefecture number 
prefecture_number = '2'

# select the table and prefecture option 
form_table = driver.find_element(By.ID, 'prefecture')
select_prefecture = form_table.find_element(By.CSS_SELECTOR, 'option:nth-child({})'.format(prefecture_number))
select_prefecture.click()
print('Starting: ' + str(select_prefecture.text))

