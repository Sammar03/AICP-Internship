import pandas as pd;
import matplotlib.pyplot as plt;

# Data to Plot
list = {
    "math_marks": [88,92,80,89,100,80,60,100,80,34],
    "science_marks": [35,79,79,48,100,88,32,45,20,30],
    "marks_range" : [10,20,30,40,50,60,70,80,90,100]
}

# Creating  Data Frame
df = pd.DataFrame(list)

# Creating a Scatter Plot
plt.scatter(df['marks_range'],df['math_marks'], color='red', label="Math marks")
plt.scatter(df['marks_range'], df['science_marks'], color = 'green', label="Science marks")

# Setting the Labels and the Title of the Graph
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Scatter plot of Marks Obtained")
plt.legend(loc = 'upper right')
plt.show()