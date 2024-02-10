import pandas as pd;
import numpy as np;



# Series without using the Dictionary (Task 1)
ser = pd.Series([1,4,9,6,7], index =['a','x','c',2,'e'])
print("Series without usinng the Dictionary:\n",ser)

# Series using the Dictionary (Task 2)
data = {'Bilal':42,'Ayesha':38,'Hadia':39}
use_dict = pd.Series(data)
print("Series using the Dictionary:\n",use_dict)

# Creation of Dataframe (Task 3)
we = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df = pd.DataFrame(we)
print("The required Dataframe using Dictionary:\n",df)

# Replacing the Index of the Dataframe (Task 4)
index_new = ['a','b','c','d','e','f']
df.index = index_new
print("Dataframe After Changing the Index:\n", df)

# Calculating the Mean, Max and Min value of Temperature column (Task 5)
mean = df['temperature'].mean()
max = df['temperature'].max()
min = df['temperature'].min()
print("The Mean of the Temperature:\t",mean)
print("The Max of the Temperature:\t",max)
print("The Min of the Temperature:\t",min)