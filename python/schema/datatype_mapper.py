import pandas as pd


def map_dtype(dtype):
    """
    Maps Pandas data types to Snowflake data types.
    """

    if pd.api.types.is_integer_dtype(dtype):
        return "NUMBER"

    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"

    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"

    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"

    else:
        return "STRING"