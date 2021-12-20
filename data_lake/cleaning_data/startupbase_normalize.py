import pandas as pd
from sqlalchemy import create_engine
from collections import Counter
from dotenv import load_dotenv
import os

df = pd.read_parquet('./raw_data/startup.parquet')

print(df)

df['name'] = df['name'].str.lower().str.strip()
df['cidade_estado'] = df['cidade_estado'].str.lower().str.strip()
df['mercado'] = df['mercado'].str.lower().str.strip()
df['modelo'] = df['modelo'].str.lower().str.strip()
df['modelo de receita'] = df['modelo de receita'].str.lower().str.strip()
df['momento'] = df['momento'].str.lower().str.strip()


print(df)

df['estado'] = ['' for row in df['name']]
df['cidade'] = ['' for row in df['name']]

for i in range(len(df['name'])):
    ci_es = df['cidade_estado'][i]
    ci_es = str(ci_es).split(' - ')
    print(ci_es)
    if len(ci_es) >= 2:
        df['estado'][i] = ci_es[1]
        df['cidade'][i] = ci_es[0]


print(df['estado'])

