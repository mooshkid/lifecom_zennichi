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


# japan prefecture tuplets 
prefectures = [('01', '北海道'), ('02', '青森県'), ('03', '岩手県'), ('04', '宮城県'), ('05', '秋田県'), ('06', '山形県'), ('07', '福島県'), ('08', '茨城県'), ('09', '栃木県'), ('10', '群馬県'), ('11', '埼玉県'), ('12', '千葉県'), ('13', '東京都'), ('14', '神奈川県'), ('15', '山梨県'), ('16', '新潟県'), ('17', '富山県'), ('18', '石川県'), ('19', '福井県'), ('20', '長野県'), ('21', '岐阜県'), ('22', '静岡県'), ('23', '愛知県'), ('24', '三重県'), ('25', '滋賀県'), ('26', '京都府'), ('27', '大阪府'), ('28', '兵庫県'), ('29', '奈良県'), ('30', '奈良県'), ('31', '鳥取県'), ('32', '島根県'), ('33', '岡山県'), ('34', '広島県'), ('35', '山口県'), ('36', '徳島県'), ('37', '香川県'), ('38', '愛媛県'), ('39', '高知県'), ('40', '福岡県'), ('41', '佐賀県'), ('42', '長崎県'), ('43', '熊本県'), ('44', '大分県'), ('45', '宮崎県'), ('46', '鹿児島県'), ('47', '沖縄県') ]


# loop all prefectures 
for i in prefectures:

    # empty lists 
    td_name_list = []
    td_details_list = []

    # indexing tuples
    pref_num = i[0]
    pref_name = i[1]

    # webdriver 
    url = 'https://www.zennichi.or.jp/member_search/list/?prefecture={}&branch=&address=&representative=&shogo=&shogo_kana=&license_holder=&number=&region=&hosho_approved='.format(pref_num)
    driver = webdriver.Chrome()
    driver.get(url)

    # find prefecture name
    print('Starting: (' + pref_num + ')' + pref_name + '...')

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
            time.sleep(2)

    # once last time for the last page, since it doesn't have the next button
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

    time.sleep(2)
    driver.close()

    # dictionary of lists  
    dict = {'name': td_name_list, 'details': td_details_list}  
    df = pd.DataFrame(dict) 
        
    # saving the dataframe 
    df.to_csv(pref_name + '.csv') 

    print('Finished ' + pref_name)
    time.sleep(2)

print('Completed')