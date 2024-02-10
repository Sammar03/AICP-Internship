import pandas as pd;
import numpy as np;

# Importing Data from a single sheet of an Excel file and setting row 2 as the Header
ask = pd.read_excel("Datasets/SampleWork.xlsx", sheet_name="Sheet1",skiprows=2)

# Selecting only the First and the Last column from the Excel file
ask1 = ask.iloc[:,[0,-1]]
print(ask1)

# Exporting the Data into another Sheet(New Sheet) in the existing excel file
with pd.ExcelWriter("Github/AICP-Internship/Week 2/Data/SampleWork.xlsx", mode = "a") as writer:
    ask1.to_excel(writer, sheet_name="New Sheet")