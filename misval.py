import pandas as pd

df=pd.read_csv('data.csv')
percent_missing = df.isnull().sum() * 100 / len(df)
print(df.fillna("N/A"))
print(percent_missing)
