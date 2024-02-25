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

# Plot all 10 columns in the same page
plt.figure(figsize=(20, 12))  # Set figure size
for i, column in enumerate(cols, 1):
    plt.subplot(2, 5, i)  # Create subplot
    sns.stripplot(x='Category', y=column, data=df, hue="Category")
    plt.title(f'{column} Content', fontsize=8)  # Decrease title font size
    plt.xlabel('Category', fontsize=6)  # Decrease x-axis label font size
    plt.ylabel(column, fontsize=6)  # Decrease y-axis label font size
    plt.xticks(rotation=45, fontsize=6)  # Rotate x-axis labels and decrease font size
    plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent overlap of subplots
plt.show()  # Show all plots in the same page

# Get unique categories
categories = df['Category'].unique()

# Plot horizontal bar charts for items in each category
for category in categories:
    # Filter the DataFrame for the current category
    category_df = df[df['Category'] == category]
    
    # Plot a horizontal bar chart for the items in the category
    plt.figure(figsize=(10, 6))
    plt.barh(category_df['Item'], category_df['Calories'], color='skyblue')
    plt.xlabel('Calories', fontsize=5)
    plt.ylabel('Item', fontsize=5)
    plt.title(f'Calories in {category}')
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest value at the top
    plt.tight_layout()
    plt.show()
