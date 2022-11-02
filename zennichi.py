from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import os
import time
import csv

# start timer 
start = time.time()
# counter 
count = 1

# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()



# prefecture number 1~47
prefecture_number = '37'

# webdriver 
url = 'https://www.zennichi.or.jp/member_search/list/?prefecture={}&branch=&address=&representative=&shogo=&shogo_kana=&license_holder=&number=&region=&hosho_approved='.format(prefecture_number)
driver = webdriver.Chrome()
driver.get(url)

# prefecture name
prefecture = driver.find_element(By.XPATH, '//*[@id="prefecture"]/option[@selected="selected"]').text
print('Starting: ' + str(prefecture) + '...')

data_all = []

try:
    while driver.find_element(By.CLASS_NAME, 'next-btn'):

        # table
        member_result_table = driver.find_element(By.CLASS_NAME, 'member-result-table')
        # tr 
        rows = member_result_table.find_elements(By.CSS_SELECTOR, 'tr')

        for row in rows[:2]:
            td_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)')
            print(str(td_name.text))
            print('\n')
            
            td_details = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
            print(str(td_details.text))
            print('----------')

            td1 = str(td_name.text)
            td2 = str(td_details.text)

            df = pd.DataFrame([td1, td2])
            data_all.append(df)
            


        next_button = driver.find_element(By.CLASS_NAME, 'next-btn')
        next_button.click()
        time.sleep(1)

except NoSuchElementException:
    # table
    member_result_table = driver.find_element(By.CLASS_NAME, 'member-result-table')
    # tr 
    rows = member_result_table.find_elements(By.CSS_SELECTOR, 'tr')

    for row in rows:
        td_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)')
        print(str(td_name.text))
        print('\n')
        
        td_details = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
        print(str(td_details.text))
        print('Finished')
        print('\n')


# fix here
        data_all.to_csv()