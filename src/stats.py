"""
This module contains a function to calculate the mean, min, and max of the 
'TemperatureC' and 'Humidity' columns in a DataFrame.
"""

import pandas as pd

def calculate_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the mean, min, and max of the 'TemperatureC' and 'Humidity' columns.

    Parameters:
    df (pd.DataFrame): A DataFrame containing the columns 'TemperatureC' and 'Humidity'.

    Returns:
    pd.DataFrame: A DataFrame with the mean, min, and max of the 
    'TemperatureC' and 'Humidity' columns.
    """
    stats = df[["TemperatureC", "Humidity"]].agg(["mean", "min", "max"])
    return stats
