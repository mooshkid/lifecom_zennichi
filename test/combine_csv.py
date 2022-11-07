import pandas as pd
import glob
import os


# output csv file name 
output_csv = 'all_name.csv'
# remove old csv file 
if os.path.exists(output_csv):
    os.remove(output_csv)
else:
    pass

# empty df 
all_data = []


csv_files = glob.glob("results/20221104/*.csv", recursive=True)

for i in csv_files:
    df = pd.read_csv(i, header=0, usecols=[1])
    all_data.append(df)


# concatenate dataframes 
all_data = pd.concat(all_data)

# reset index
all_data.reset_index(drop=True, inplace=True)

# output to csv 
# all_data.to_csv('name_all.csv', mode='a') #with index
all_data.to_csv(output_csv, mode='a', index=False) #without index
