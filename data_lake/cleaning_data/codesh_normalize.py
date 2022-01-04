import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from unidecode import unidecode
import os
import json

# 'name', 'cidade', 'contato', 'stacks', 'mercado', 'tamanho', 'redes', 'website'

df = pd.read_parquet('./raw_data/codesh.parquet')

df['name'] = df['name'].str.lower().str.strip()
""" city_json = dict()
for i, city in enumerate(df['cidade']):
    if not city.isascii():
        city = city.lower()
        city_json[city] = unidecode(city.lower().strip())
        df['cidade'][i] = unidecode(city.lower().strip())
    else:
        df['cidade'][i] = city.lower().strip() """

# print(json.dumps(city_json, indent=2))
for i, lst in enumerate(df['stacks'].values):
    df['stacks'][i] = [unidecode(string.lower().strip()) for string in df['stacks'][i]]
df['mercado'] = [unidecode(string.lower().strip()) for string in df['mercado'].values]

""" def narray_colunm_to_list(column: pd) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None

mercado_json = dict()
for i, mercado in enumerate(df['mercado']):
    if not mercado.isascii():
        mercado = mercado.lower()
        mercado_json[mercado] = unidecode(mercado.lower().strip())
        df['mercado'][i] = unidecode(mercado.lower().strip())
    else:
        df['mercado'][i] = mercado.lower().strip() """
print(df['cidade'].str.strip().str.lower())
