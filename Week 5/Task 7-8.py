import pandas as pd;
import plotly.express as px;
import plotly.graph_objects as go;
import plotly.io as pio;
pio.templates.default = "plotly_white"

# Open the 'Instagram data.csv' file in read mode with Latin-1 encoding
with open("Github/AICP-Internship/Week 5/Data/Instagram data.csv", 'r', encoding='latin1') as f:
    # Read the data from the CSV file into a pandas DataFrame
    data = pd.read_csv(f)


# Task 7: Create a pie chart to visualize reach from different sources
labels = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
values = [data['From Home'].sum(), data['From Hashtags'].sum(), data['From Explore'].sum(), data['From Other'].sum()]
colors = ['lightsalmon', 'lightpink', 'lightyellow', 'lightblue']

fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20)
fig.update_layout(title_text="Reach from Different Sources")
# Show the plot
fig.show()


# Task 8: Create a pie chart to visualize engagement sources
labels = ['Likes', 'Saves', 'Shares', 'Comments']
values = [data['Likes'].sum(), data['Saves'].sum(), data['Shares'].sum(), data['Comments'].sum()]
colors = ['lightsalmon', 'lightpink', 'lightyellow', 'lightblue']

fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20)
fig.update_layout(title_text="Engagement Sources")
# Show the plot
fig.show()
