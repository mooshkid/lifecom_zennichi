import pandas as pd
import glob
import os


# output csv file name 
output_csv = 'all_details.csv'


# user input yes/no
yes_choices = ['yes', 'y']
no_choices = ['no', 'n']

# if .csv file already exists 
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


# empty df 
all_data = []

# select all .csv files in directory 
csv_files = glob.glob("results/20221104/*.csv", recursive=True)

for i in csv_files:
    # select column with usecols=[]
    # [0] = index, [1] = name, [2] = details 
    df = pd.read_csv(i, header=0, usecols=[2])
    all_data.append(df)


# concatenate dataframes 
all_data = pd.concat(all_data)

# reset index
all_data.reset_index(drop=True, inplace=True)

# output to csv 
# all_data.to_csv('name_all.csv', mode='a') #with index
all_data.to_csv(output_csv, mode='a', index=False) #without index
