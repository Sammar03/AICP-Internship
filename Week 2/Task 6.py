import pandas as pd;
import numpy as np;

person = pd.read_csv("Datasets/people.csv", usecols=["First Name","Sex","Email","Phone","Job Title"], index_col=["Sex","Job Title"],skiprows=[1,5])
print(person.head(5))

# person.to_csv("Datasets/NewPeople.csv")