import pandas as pd
csv_url = "ai4i2020.csv"

data = pd.read_csv(csv_url)


data = data.drop(["Tool wear [min]", "TWF", "HDF", "PWF", "OSF", "RNF"], axis=1)
print(data.columns)
print(data.head())