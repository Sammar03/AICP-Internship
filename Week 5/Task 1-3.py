import pandas as pd;

# Open the 'Instagram data.csv' file in read mode with Latin-1 encoding
with open("Github/AICP-Internship/Week 5/Data/Instagram data.csv", 'r', encoding='latin1') as f:
    # Read the data from the CSV file into a pandas DataFrame
    data = pd.read_csv(f)

# Task 1: Print the column names of the DataFrame
print(data.columns)

# Task 2: Print the descriptive statistics of the DataFrame
print(data.describe())

# Task 3: Check for missing values in the DataFrame and print the result
missing_value = data.isnull().any()
print(missing_value)
