import pandas as pd;
import numpy as np;

# Importing some columns of Data from a CSV file and changing the index columns 
person = pd.read_csv("Datasets/people.csv", usecols=["First Name","Sex","Email","Phone","Job Title"], index_col=["Sex","Job Title"],skiprows=[1,5])
print(person.head(5))

# Exporting the Retrieved Data into a CSV file called "NewPeople"
person.to_csv("Github/AICP-Internship/Week 2/Data/NewPeople.csv")




