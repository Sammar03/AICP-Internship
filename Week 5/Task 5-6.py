import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Set the default template to 'plotly_white' for plots
pio.templates.default = "plotly_white"

# Open the 'Instagram data.csv' file in read mode with Latin-1 encoding
with open("Github/AICP-Internship/Week 5/Data/Instagram data.csv", 'r', encoding='latin1') as f:
    # Read the data from the CSV file into a pandas DataFrame
    data = pd.read_csv(f)


# Task 5: Plot Impressions over time
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Impressions'], mode='lines', name='Impressions', line=dict(color='blue')))
fig.update_layout(title='Impressions Over Time',
                  xaxis_title='Impressions', yaxis_title='Index', legend=dict(x=0.02, y=0.95))
# Show the plot
fig.show()


# Task 6: Plot metrics (Likes, Saves, Follows) over time
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Likes'], mode='lines', name='Likes', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=data.index, y=data['Saves'], mode='lines', name='Saves', line=dict(color='red')))
fig.add_trace(go.Scatter(x=data.index, y=data['Follows'], mode='lines', name='Follows', line=dict(color='green')))
fig.update_layout(title='Metrics Over Time',
                  xaxis_title='Count', yaxis_title='Date', legend=dict(x=0.02, y=0.95))
# Show the plot
fig.show()
