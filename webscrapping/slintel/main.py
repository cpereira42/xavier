import pandas as pd

df = pd.read_parquet('../data_files/startup.parquet')



companies = df['name'].to_list()
companies = [company.lower() for company in companies]
print(df)
print(companies)
