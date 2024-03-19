import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


# Setting default plotly template
pio.templates.default = "plotly_white"

# Read the data from the CSV file into a DataFrame
with open("Github/AICP-Internship/Week 5/Data/Instagram data.csv", 'r', encoding='latin1') as f:
    data = pd.read_csv(f)


# Task 11: Calculate and visualize the correlation matrix
corr_cols = data.drop(['Caption', 'Hashtags'], axis=1)  # Remove non-numeric columns for correlation calculation
corr1 = corr_cols.corr()  # Calculate correlation matrix
fig = px.imshow(corr1, color_continuous_scale='Blues')  # Plot correlation matrix
fig.show()  # Show the plot


# Task 12: Visualize counts of hashtags
counts = data['Hashtags'].str.findall(r'(#\w+)').explode().value_counts()  # Count hashtags
we = counts.reset_index()  # Reset index for plotting
we.columns = ['Hashtag', 'Count']  # Rename columns
fig = px.bar(we, x='Hashtag', y='Count')  # Plot bar chart
fig.show()  # Show the plot