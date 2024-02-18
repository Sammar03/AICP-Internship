import matplotlib.pyplot as plt;
import pandas as pd;


# Task 4
#  Data for plot
prog_lang = ["Java","Python","PHP","JavaScript","C#","C++"]
popularity = [22.2,17.6,8.8,8,7.7,6.7]

# Creating a Horizontal Bar Chart
plt.barh(prog_lang,popularity, color = 'g')

# Adding grid lines with custom parameters
plt.grid(which='both',axis='both', color='red',linestyle='--',linewidth=0.5,alpha=0.5)

# Adding Labels to the Graph
plt.xlabel("Popularity")
plt.ylabel("Programming Language")

plt.title("Popularity of Programming Languages Worldwide, Oct 2017")

plt.show()


# Task 5
# Data for the Plot
we = {
    "a" : [4,2,4,2,2],
    "b" : [8,3,7,6,4],
    "c" : [5,4,4,4,3],
    "d" : [7,2,7,8,3],
    "e" : [6,6,8,6,2]
}

# Creating a Data Frame
df = pd.DataFrame(we)
index_col = [2,4,6,8,10]
colours = ['blue','green','red', 'cyan','purple']

# Setting the index_col as the Index of the Data Frame
df.set_index(pd.Index(index_col), inplace=True)

# Plotting the Data Frame
df.plot(kind ='bar', alpha= 0.9,  color= colours,figsize=(10,6))
plt.ylim(0, df.values.max())
plt.grid(True, which='both',axis='both', color='green',linestyle='--',linewidth=0.5,alpha=0.5)

plt.show()



