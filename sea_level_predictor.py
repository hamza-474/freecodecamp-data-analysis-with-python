import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    DATA_FILE = 'epa-sea-level.csv'
    DATA_URL = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv'
    DATA_PATH = DATA_FILE if os.path.exists(DATA_FILE) else (os.path.join('data', DATA_FILE) if os.path.exists(os.path.join('data', DATA_FILE)) else DATA_URL)
    df = pd.read_csv(DATA_PATH)
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit (all data, extended to 2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, color='red')
    # Create second line of best fit (data from year 2000, extended to 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    ax.plot(x_pred_recent, y_pred_recent, color='green')
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    # Save plot and return the axes
    fig.savefig('sea_level_plot.png')
    return ax
