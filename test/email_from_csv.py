import csv
import re

email_list = []

with open('./20221104/all_details.csv', newline='') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    for row in reader:

        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        match = pattern.findall(row[0])

        if match:
            email_list.append(match)


with open('email.csv', 'a') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerows(email_list)
