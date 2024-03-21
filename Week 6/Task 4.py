# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Read the dataset from CSV file
data = pd.read_csv("Github/AICP-Internship/Week 6/Data/births.csv")

# Extract decade from 'year' column and create a new column 'decade'
we = (data['year'] // 10) * 10
data['decade'] = we

# Define function to fill missing 'day' values sequentially from 1 to 31
def fill_days(data):
    day = 1
    for i in data.index:
        if pd.isnull(data.loc[i, 'day']):
            data.loc[i, 'day'] = day
            day += 1
            if day > 31:
                day = 1
    return data

# Fill missing 'day' values in the dataset
data = fill_days(data)

# Task 4: Plot trend of male & female births every decade
grouped = data.groupby(['gender', 'decade'])['births'].sum().reset_index()  # Group data by gender and decade, summing up births
pivot_df = grouped.pivot(index='decade', columns='gender', values='births')  # Pivot table for plotting
ax = pivot_df.plot(kind='line')  # Plotting line chart

# Format the y-axis to display values in millions
def y_fmt(x, pos):
    s = f'{x * 1e-6:,.1f}M'
    return s

ax.yaxis.set_major_formatter(ticker.FuncFormatter(y_fmt))  # Apply formatter to y-axis

# Define labels and title for the plot
plt.xlabel('Decade')
plt.ylabel('Number of Births')
plt.title('Trend of Male & Female Births Every Decade')
plt.show()