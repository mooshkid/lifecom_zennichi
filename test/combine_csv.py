import pandas as pd
import glob


csv_files = glob.glob("results/20221104/*.csv", recursive=True)


all_data = []

for i in csv_files:
    df = pd.read_csv(i, header=0, usecols=[1])
    all_data.append(df)

all_data = pd.concat(all_data)
all_data.to_csv('all.csv', index=False, mode='a')
