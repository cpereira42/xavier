from selenium_bot import startupbase
from beautiful_bot import startup_infos
from pyarrow import parquet as pq
import pyarrow as pa
import pandas as pd
import numpy as np


def get_all_pages_data(soup, bodys: list):
    data = list()
    for body in bodys:
        try:
            data.append(soup.get_all_infos(body))
        except BaseException:
            pass
    return data


with startupbase() as driver:
    driver.land_page()
    driver.scroll_down()
    links = driver.get_page_links()
    bodys = driver.get_body_requests(links)

soup = startup_infos()
data = get_all_pages_data(soup, bodys)

df = pd.DataFrame(
    np.array(data),
    columns=[
            'NAME', 'ESTADO', 'MERCADO', 'MODELO', 'MODELO DE RECEITA',
            'MOMENTO', 'TAMANHO', 'SEGMENTO', 'REDES'])

table = pa.Table.from_pandas(df)
pq.write_table(table, 'startup.parquet')