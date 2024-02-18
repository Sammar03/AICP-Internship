import pandas as pd;
import matplotlib.pyplot as plt;


# Task 1
# Values of x-axis and y-axis
x_axis = [1.0,1.5,2.0,2.5,3.0 ]
y_axis = [2.0,3.0,4.0,2.5,1.0]

# Plotting the Values
plt.plot(x_axis, y_axis)

# Labelling the x-axis and the y-axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Setting the limits of the x-axis and the y-axis
plt.xlim(min(x_axis),max(x_axis))
plt.ylim(min(x_axis),max(y_axis))

# Labelling the title of the Graph
plt.title("Plot Between the Values of X-axis and Y-axis using Matplotlib")

# Displaying the Graph
plt.show()


# Task 2
# Values of x_axis and y-axis
x1 = [10,15,20,25,30]
y1 = [20,30,40,25,10]
y2 = [40,26,10,20,30]

# Plotting the lines
plt.plot(x1, y1, label="Line 1 with width 3", linewidth = 3, color = "black")
plt.plot(x1, y2, label="Line 2 with width 5", linewidth = 5, color = "yellow")

# Setting the limits of the x_axis and y_axis
plt.xlim(min(x1), max(x1))
plt.ylim(min(y2), max(y1))

# Labelling the x_axis and y_axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Giving the Title of the graph
plt.title("Plotting multiple lines in the same graph")

# Showcasing the legend
plt.legend()

# Displaying the graph
plt.show()


# Task 3
# Sample data
x_values = [1, 4, 5, 6, 7]
y_values = [2, 6, 3, 6, 3]


# Plot the line with a dotted style and specify color
plt.plot(x_values, y_values, linestyle=':', color='red')  

# Plot the big dot with a specified color
plt.plot(x_values, y_values, marker='o', markersize=8, linestyle='', color='blue')  

# Add labels for the x and y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Setting the limits for x-axis and y-axis
plt.xlim(1,8)
plt.ylim(1,8)

# Add a title to the plot
plt.title('MultipleLines with Line Markers')

# Display the plot
plt.show()








