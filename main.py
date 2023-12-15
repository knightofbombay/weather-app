# main.py

"""
This module is the main entry point of the program. It loads weather data, calculates statistics, 
and visualizes the results.
"""

from src.dataprep import load_data
from src.stats import calculate_stats
from src.visualize import plot_graphs

def main():
    """
    Main function to load data, calculate statistics, and visualize the results
    """
    # Load data
    df = load_data('weather_data.csv')

    # Calculate statistics
    stats = calculate_stats(df)
    print(stats)

    # Visualize
    plot_graphs(stats)


if __name__ == "__main__":
    main()
