import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table"

response = requests.get(url)

if response.status_code == 200:
    soup = bs(response.text, "html.parser")
    
    # Corrected class name
    table = soup.find("table", {"class": "wikitable sortable plainrowheaders jquery-tablesorter"})
    
    data = []
    for row in table.find_all('tr')[1:]:
        columns = row.find_all(['th','td'])
        country = columns[1].text.strip()  # Extract country name from the second column
        medals = columns[2].text.strip()
        data.append([country, medals])
 
    df = pd.DataFrame(data, columns=["Country", "Medals"])
    print(df.head(5))

    df.to_csv("GitHub/AICP-Internship/Week 3/Data/ Olympics2016.csv", index=False)
    print("CSV Created Successfully!")
    
else: 
    print("Failure")

