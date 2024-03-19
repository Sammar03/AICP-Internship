import pandas as pd;
import matplotlib.pyplot as plt;
import plotly.express as px;
with open("Github/AICP-Internship/Week 5/Data/Instagram data.csv", 'r', encoding='latin1') as f:
    # Read the data from the CSV file into a pandas DataFrame
    data = pd.read_csv(f)


# Task 4: Plot histogram to visualize the distribution of Impressions
fig = px.histogram(data, x="Impressions", nbins=8, title="Distribution of Impressions")
fig.update_xaxes(tickformat=".0s")  # Update x-axis tick format
fig.show()  # Show the plot
