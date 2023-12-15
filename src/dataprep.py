# dataprep.py
"""
This module contains a function to load weather data from a CSV file into a pandas DataFrame.
"""
import pandas as pd
from pandas.errors import EmptyDataError

def load_data(file_name: str) -> pd.DataFrame:
    """
    Load weather data from a CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the weather data.
    """
    try:
        df = pd.read_csv(file_name)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return pd.DataFrame()
    except EmptyDataError:
        print(f"The file '{file_name}' is empty.")
        return pd.DataFrame()
    