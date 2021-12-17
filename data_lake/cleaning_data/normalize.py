from pyarrow import parquet as pq
# import pyarrow as pa
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df = pq.read_table(source='./raw_data/thor.parquet').to_pandas()

print(df)
df['NAME'] = df['NAME'].str.lower()
for l_stacks in range(len(df['STACKS'])):
    for element in range(len(df['STACKS'][l_stacks])):
        df['STACKS'][l_stacks][element] =\
                df['STACKS'][l_stacks][element].lower()
# df['STACKS'] = df['STACKS'].str.lower()
print(df)
engine = create_engine('postgresql://ecole42_xavier:veL8^KY^wz0K\
@proj-educ-db-psql.cuozdedywi38.us-west-2.rds.amazonaws.com:5432/ecole42_xavier')

df.to_sql('Empresa_thor', engine, if_exists='replace', index=False)
conn = engine.raw_connection()
cur = conn.cursor()
conn.commit()


"""
host=proj-educ-db-psql.cuozdedywi38.us-west-2.rds.amazonaws.com
user=ecole42_xavier
pass=veL8^KY^wz0K
port=5432
dbname=ecole42_xavier
"""