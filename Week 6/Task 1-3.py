# Importing necessary libraries
import pandas as pd
import numpy as np

# Read the dataset from CSV file
data = pd.read_csv("Github/AICP-Internship/Week 6/Data/births.csv")


# Task 1: Create a new column 'decade' representing the decade of each year
we = (data['year'] // 10) * 10
data['decade'] = we

# Task 2: Print descriptive statistics of the dataset
print(data.describe())

# Task 3: Check for missing values in the dataset
missing = data.isnull().any()
print(missing)

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
