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

# Cleaning the Data

# Filter out days exceeding 31
filter_1 = data['day'] <= 31
data = data[filter_1]

# Filter out days based on month's days (28, 30, 31)
filter_2 = ((data['month'].isin([1, 3, 5, 7, 8, 10, 12]) & (data['day'] <= 31)) |
            (data['month'].isin([4, 6, 9, 11]) & (data['day'] <= 30)) |
            (data['month'] == 2 & (data['day'] <= 28 + (data['year'] % 4 == 0))))
data = data[filter_2]

# Task 5: Filtering data based on mean and standard deviation
mean = data['births'].mean()
std_dev = data['births'].std()
range = 5
filter_3 = np.abs(data['births'] - mean) <= (range * std_dev)
filtered = data[filter_3]
print(filtered.describe())

# Task 6: Grouping and plotting births by gender and weekday
data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
data['weekday'] = data['date'].dt.dayofweek
weekday_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
data['weekday'] = data['weekday'].map(weekday_map)
grouped = data.groupby(['gender', 'weekday'])['births'].sum().reset_index()
pivot_df = grouped.pivot(index='weekday', columns='gender', values='births')
ax = pivot_df.plot(kind='line')

def y_fmt(x, pos):
    s = f'{x * 1e-6:,.1f}M'
    return s

ax.yaxis.set_major_formatter(ticker.FuncFormatter(y_fmt))
plt.show()

# Task 7: Grouping births by day and month for filtered data
by_day = filtered.groupby('day')['births'].sum().reset_index()
print(by_day)

by_month = filtered.groupby('month')['births'].sum().reset_index()
print(by_month)

# Task 8: Plotting mean births by time series
data['date'] = pd.to_datetime(data.assign(year=2012)[['year', 'month', 'day']])
grouped = data.groupby(data['date'].dt.strftime('%m-%d'))['births'].mean()
plt.figure(figsize=(10, 5))
plt.plot(grouped)
plt.show()
