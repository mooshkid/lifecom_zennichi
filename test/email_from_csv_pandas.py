import pandas as pd
import re

# empty list 
email_list = []


df = pd.read_csv('./all_details.csv')

for row in df.iterrows():

    pattern = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com")
    match = pattern.match(str(row))

    if match:
        email_list.append(row)

print(email_list)
# email_list.to_csv('lalala.csv')



# with open('all_details.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:

#         pattern = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com")

#         match = pattern.findall(str(row))

#         if match:
#             # with open('all_details.text', 'a') as textfile:
#             #     textfile.write(str(match))
#             email_list.append(match)
#             # print(email_list)

# with open('email.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerows(email_list)