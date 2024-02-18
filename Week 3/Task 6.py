import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("GitHub/AICP-Internship/Week 3/Data/ Olympics2016.csv")

# Select top 5 countries
top5 = df.head(5)

# Calculate total gold medals for the top 5 countries
total_gold = top5["Medals"].sum()

# Calculate percentage of medals for each country
top5['Percentage'] = (top5["Medals"] / total_gold) * 100

explode = [0.1,0,0,0,0]
fig , ax = plt.subplots()
# Plot pie chart
ax.pie(top5['Percentage'], labels=top5["Country"], wedgeprops=dict(edgecolor='black'), autopct="%1.1f%%", startangle=150, explode = explode, shadow = True)

plt.title("Distribution of Gold Medals Won by Top 5 Countries in Olympics 2016")
# Show plot
plt.show()
