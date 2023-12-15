# test_stats.py
"""
This module contains tests for the load_data function in the dataprep module.
"""

import os
import sys
import pandas as pd

sys.path.append('src')
from dataprep import load_data  # noqa: E402

def test_load_data_existing_file():
    """
    Test loading data from an existing CSV file.
    """
    # Add test code here
    # Create a temporary CSV file with sample weather data
    temp_csv = "temp_weather_data.csv"
    sample_data = {
        "Date": ["2022-01-01", "2022-01-02", "2022-01-03"],
        "Temperature": [10, 15, 20],
        "Humidity": [50, 60, 70],
    }
    df = pd.DataFrame(sample_data)
    df.to_csv(temp_csv, index=False)

    # Test loading data from the temporary CSV file
    loaded_df = load_data(temp_csv)
    assert isinstance(loaded_df, pd.DataFrame)
    assert len(loaded_df) == 3
    assert loaded_df.columns.tolist() == ["Date", "Temperature", "Humidity"]

    # Clean up the temporary CSV file
    os.remove(temp_csv)


def test_load_data_nonexistent_file():
    """
    Test loading data from a nonexistent CSV file.
    """
    # Test loading data from a nonexistent CSV file
    loaded_df = load_data("nonexistent_file.csv")
    assert isinstance(loaded_df, pd.DataFrame)
    assert len(loaded_df) == 0
    assert loaded_df.columns.tolist() == []


def test_load_data_empty_file():
    """
    Test loading data from an empty CSV file.
    """
    # Create an empty CSV file
    empty_csv = "empty_weather_data.csv"
    with open(empty_csv, "w", encoding="utf-8"):
        pass

    # Test loading data from the empty CSV file
    loaded_df = load_data(empty_csv)
    assert isinstance(loaded_df, pd.DataFrame)
    assert len(loaded_df) == 0
    assert loaded_df.columns.tolist() == []

    # Clean up the empty CSV file
    os.remove(empty_csv)
