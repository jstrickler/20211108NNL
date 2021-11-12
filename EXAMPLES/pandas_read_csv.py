import pandas as pd

df = pd.read_csv('../DATA/sales_records.csv')  # <.>

print(df.describe())  # <.>
print()

print(df.info())  # <.>
print()

print(df.head())  # <.>

df['Unit Cost'] /= 2

df.to_csv('salesdata_out.csv')
