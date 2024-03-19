# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from sklearn.linear_model import LinearRegression
from wordcloud import WordCloud as wc

# Setting default plotly template
pio.templates.default = "plotly_white"

# Read the data from the CSV file into a DataFrame
with open("Github/AICP-Internship/Week 5/Data/Instagram data.csv", 'r', encoding='latin1') as f:
    data = pd.read_csv(f)


# Task 9: Fit a linear regression model to Profile Visits vs. Follows data
x = data['Profile Visits'].values.reshape(-1, 1)
y = data['Follows'].values
model = LinearRegression()  # Initialize linear regression model
model.fit(x, y)  # Fit the model
y_pred = model.predict(x)  # Predict y values for the line of best fit
scatter = go.Scatter(x=data['Profile Visits'], y=data['Follows'], mode='markers', name='Data')  # Scatter plot for original data
line = go.Scatter(x=data['Profile Visits'], y=y_pred, mode='lines', name='Fit')  # Line plot for line of best fit
layout = go.Layout(title='Profile Visits vs. Follows', xaxis=dict(title='Profile Visits'), yaxis=dict(title='Follows'))  # Layout for the plot
fig = go.Figure(data=[scatter, line], layout=layout)  # Combine scatter and line plots
fig.show()  # Show the plot


# Task 10: Generate a word cloud for the Hashtags column
hash = data['Hashtags'].values
text = ' '.join(hash)
cloud = wc().generate(text)  # Generate word cloud
plt.imshow(cloud, interpolation='bilinear')  # Display word cloud
plt.show()


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
