import csv
import re
import os

# file names
input_csv = './20221104/prefectures_all.csv'
output_csv = 'prefectures_all_email.csv'

email_list = []

with open(input_csv, newline='') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    for row in reader:

        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        match = pattern.findall(row[2]) #2 is the details row

        if match:
            email_list.append(match)


# user input yes/no
yes_choices = ['yes', 'y']
no_choices = ['no', 'n']

if os.path.exists(output_csv):
    while True:
        user_input = input('The file "' + output_csv + '" already exists. Would you like to override it? (yes/no): ')
        if user_input.lower() in yes_choices:
            os.remove(output_csv)
            break
        elif user_input.lower() in no_choices:
            new_csv_name = input('Please enter a new file name: ')
            output_csv = new_csv_name + '.csv'
            break
        else:
            continue
else:
    pass

with open(output_csv, 'a') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerows(email_list)
