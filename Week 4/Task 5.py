# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the DataFrame from CSV file
df = pd.read_csv("Github/AICP-Internship/Week 4/Data/menu.csv")

# Define columns of interest
cols = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)', 'Iron (% Daily Value)']

# Get the maximum value from each column
max_values = df[cols].max(axis=0)

# Iterate over the columns
for column, max_value in max_values.items():
    # Find the index of the row containing the maximum value for the current column
    index = df[column].idxmax()
    
    # Get the name of the item from the 'Category' column using the index
    item = df.loc[index, 'Item']
    
    # Print the column name, maximum value, and corresponding item name
    print(f"{column}: {item} - {max_value}")
