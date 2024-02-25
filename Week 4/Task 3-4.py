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

# Calculating correlation matrix between selected columns
corr_we = use.corr()

# Generating heatmap for correlation matrix
plt.figure(figsize=(8,6))
sns.heatmap(corr_we)
plt.title("Correlation Plot Between Calories and Other Quantities")
plt.tight_layout()
plt.show()

# Generating boxplot of 'Calories' grouped by 'Category'
df.boxplot(column=['Calories'], by='Category', vert=False, showcaps=False)

# Adding labels and formatting to the boxplot
plt.xlabel("Category")
plt.ylabel("Calories")
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.show()
