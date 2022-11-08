import csv
import re

email_list = []

with open('all_details.csv', newline='') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    for row in reader:

        pattern = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com")
        match = pattern.findall(row[0])

        if match:
            email_list.append(match)


with open('email.csv', 'a') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerows(email_list)
