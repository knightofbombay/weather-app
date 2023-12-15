#test_stats.py
"""
This module contains tests for the calculate_stats function in the stats module.
"""

import os
import sys
import pandas as pd

sys.path.append('src')
from stats import calculate_stats


def test_calculate_stats():
    """
    Test the calculate_stats function.
    """
    # Create a sample DataFrame
    sample_data = {
        "TemperatureC": [10, 15, 20],
        "Humidity": [50, 60, 70],
    }
    df = pd.DataFrame(sample_data)

    # Calculate the stats using the calculate_stats function
    stats = calculate_stats(df)

    # Check the calculated stats
    assert isinstance(stats, pd.DataFrame)
    assert len(stats) == 3
    assert stats.columns.tolist() == ["TemperatureC", "Humidity"]
    assert stats.loc["mean", "TemperatureC"] == 15
    assert stats.loc["mean", "Humidity"] == 60
    assert stats.loc["min", "TemperatureC"] == 10
    assert stats.loc["min", "Humidity"] == 50
    assert stats.loc["max", "TemperatureC"] == 20
    assert stats.loc["max", "Humidity"] == 70
