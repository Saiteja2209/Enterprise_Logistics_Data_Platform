import pandas as pd

from python.schema.datatype_mapper import map_dtype

df = pd.DataFrame({
    "id": [1],
    "name": ["Sai"],
    "salary": [1000.5],
    "active": [True],
    "created": [pd.Timestamp("2026-07-23")]
})

for column in df.columns:
    print(column, "->", map_dtype(df[column].dtype))