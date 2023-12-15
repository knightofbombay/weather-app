# visualize.py
"""
This module contains a function to plot graphs for Temperature and Humidity.
"""

import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt  # noqa: E402


def plot_graphs(stats_df: pd.DataFrame) -> matplotlib.figure.Figure:
    """
    Plot graphs for Temperature and Humidity.

    Parameters:
    stats_df (pd.DataFrame): A DataFrame containing 'TemperatureC' and 'Humidity' columns.

    Returns:
    matplotlib.figure.Figure: The Figure object with the plotted graphs.
    """
    fig, (ax1, ax2) = plt.subplots(2)

    # Plot onto axes
    stats_df["TemperatureC"].plot(ax=ax1)
    stats_df["Humidity"].plot.bar(ax=ax2)

    ax1.set_ylabel("Temperature (C)")
    ax2.set_ylabel("Humidity %")

    # Display plots
    plt.tight_layout()
    plt.show()

    return fig
