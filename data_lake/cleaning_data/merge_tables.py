import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv('../../login.env')
host = getenv('DBHOST')
user = getenv('DBUSER')
passwd = getenv('DBPASS')
port = getenv('DBPORT')
database = getenv('DBNAME')

engine = create_engine(f'postgresql://{user}:{passwd}\
@{host}:{port}/{database}')

df = pd.DataFrame()

df_startup = pd.read_sql('startupBase', engine)
df = df_startup
df_thor = pd.read_sql('programathor', engine)


def narray_colunm_to_list(column: pd) -> None:
    for i in range(len(column)):
        column[i] = column[i].tolist()
    return None


def show_equals(column_1, column_2):
    result = []
    for i in column_1:
        for j in column_2:
            if i == j:
                result.append(i)
    return result


df['stacks'] = [[] for _ in df['name']]

equal_l = show_equals(df_thor['name'], df_startup['name'])
for i, name in enumerate(df['name']):
    if name in equal_l:
        print(df_thor.loc[df_thor['name'] == name]['stacks'])

# df['stacks'] = [str(i) for i in df['stacks']]
# df = df.drop(columns=['stacks'])
# df.to_sql('main', engine, if_exists='replace', index=False)
