from thor_bot import get_all
from pyarrow import parquet as pq
import pyarrow as pa
import pandas as pd
import numpy as np

data = get_all()
df = pd.DataFrame(
    np.array(data),
    columns=[
            'NAME', 'STACKS'])

table = pa.Table.from_pandas(df)
pq.write_table(table, 'thor.parquet')
