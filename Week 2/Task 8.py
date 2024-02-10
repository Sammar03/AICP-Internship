import pandas as pd;
import numpy as np;



df = {
    "Name": ["Sonia","Bilal","Hifza","Kabir","jazim"],
    "Age": [27,24,22,32,23],
    "Address": ["Lahore","Karachi","Sialkot","Peshawar","lhr"],
    "Qualification": ["Msc","MA","MCA","PHD","bsc"]
}

# Creating the AICP_DF Dataframe
AICP_DF = pd.DataFrame(df)
print("The AICP_DF Dataframe:\n",AICP_DF)

# Creating the df1 Dataframe
df1 = AICP_DF[["Name","Qualification"]]
print("The df1 Dataframe:\n",df1)

# Adding a new column "Height" into the AICP_DF Dataframe
AICP_DF["Height"] = [5.1,6.2,5.1,5.2,5.1]
print("AICP_DF after addition of Heigh column:\n",AICP_DF)

# Setting the "Name" column as the Index column of the AICP_DF Dataframe
AICP_DF.set_index("Name", inplace=True)
print("AICP_DF after settign the Name column as Index:\n",AICP_DF)

# Retreiving the row with "Hifza" as the Index element from the AICP_DF Dataframe
print("The row with Index Hifza from AICP_DF:\n",AICP_DF[AICP_DF.index == "Hifza"])

# Retrieving the row with Index 3 from the df1 Dataframe
print("Row with Index 3 from df1:\n",df1[df1.index == 3])

# Dropping the row with "Bilal" as Index Element
AICP_DF = AICP_DF.drop("Bilal")
print("AICP_DF after dropping row with Index Bilal:\n",AICP_DF)