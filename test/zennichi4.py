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


prefecture_range = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                    '41', '42', '43', '44', '45', '46', '47',]

# for i in range(1, 48):
for i in prefecture_range:

    # webdriver 
    url = 'https://www.zennichi.or.jp/member_search/list/?prefecture={}&branch=&address=&representative=&shogo=&shogo_kana=&license_holder=&number=&region=&hosho_approved='.format(i)
    driver = webdriver.Chrome()
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