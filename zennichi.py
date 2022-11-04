from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import os
import time

# start timer 
start = time.time()
# counter 
count = 1

# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()

# empty lists 
td_name_list = []
td_details_list = []



for i in range(1, 48):

    # prefecture number 01~47
    prefecture_number = i

    # webdriver 
    url = 'https://www.zennichi.or.jp/member_search/list/?prefecture={}&branch=&address=&representative=&shogo=&shogo_kana=&license_holder=&number=&region=&hosho_approved='.format(prefecture_number)    driver = webdriver.Chrome()
    driver.get(url)

    # prefecture name
    prefecture = driver.find_element(By.XPATH, '//*[@id="prefecture"]/option[@selected="selected"]').text
    print('Starting: ' + str(prefecture) + '...')

    try:
        while driver.find_element(By.CLASS_NAME, 'next-btn'):

            # table
            member_result_table = driver.find_element(By.CLASS_NAME, 'member-result-table')
            # tr 
            rows = member_result_table.find_elements(By.CSS_SELECTOR, 'tr')

            for row in rows[1:]:
                td_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)')
                td_name = str(td_name.text)
                td_name_list.append(td_name)
                
                td_details = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
                td_details = str(td_details.text)
                td_details_list.append(td_details)


            next_button = driver.find_element(By.CLASS_NAME, 'next-btn')
            next_button.click()
            time.sleep(1)

    except NoSuchElementException:
        # table
        member_result_table = driver.find_element(By.CLASS_NAME, 'member-result-table')
        # tr 
        rows = member_result_table.find_elements(By.CSS_SELECTOR, 'tr')

        for row in rows[1:]:
            td_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)')
            td_name = str(td_name.text)
            td_name_list.append(td_name)
            
            td_details = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
            td_details = str(td_details.text)
            td_details_list.append(td_details)


    # dictionary of lists  
    dict = {'name': td_name_list, 'details': td_details_list}  
    df = pd.DataFrame(dict) 
        
    # saving the dataframe 
    df.to_csv(str(prefecture) + '.csv') 