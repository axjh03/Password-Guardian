import csv
import pandas as pd

df = pd.read_csv('name.csv')
df = pd.DataFrame(columns=['userName'])
df.iloc[0][0] = 'Aalok'
# name = input("Enter your name: ")
print(df)