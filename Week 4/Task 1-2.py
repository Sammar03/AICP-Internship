# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Reading CSV file into a DataFrame
df = pd.read_csv("Github/AICP-Internship/Week 4/Data/menu.csv")

# Selecting specific columns from DataFrame and creating a copy
cols = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)', 'Iron (% Daily Value)']
use = df[cols].copy()

# Generating descriptive statistics for DataFrame
stats = df.describe()
print(stats)

# Finding maximum values for each column in the selected DataFrame
max_val = use.max()
print(max_val)
