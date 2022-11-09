import csv
import re

email_list = []

with open('./20221104/prefectures_all.csv', newline='') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    for row in reader:

        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        match = pattern.findall(row[2]) #2 is the details row

        if match:
            email_list.append(match)


with open('prefectures_all_email.csv', 'a') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerows(email_list)
