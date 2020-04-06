import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests 
from bs4 import BeautifulSoup 
import geopandas as gpd
from prettytable import PrettyTable


url = 'https://www.mohfw.gov.in/' 


site_content = requests.get(url).content
soup = BeautifulSoup(site_content, "html.parser")

# initialize stats
stats = [] 
# find all the rows of tablesr 
all_rows = soup.find_all('tr') 

for row in all_rows: 
    # list of length 6
    if length(stat) == 6: 
        stats.append(stat)

# converts the data into a pandas dataframe 
new_cols = ["Serial.No", "States","Confirmed","Recovered","Deaths"]
state_data = pd.DataFrame(data = stats, columns = new_cols)

# string data to int
state_data['Confirmed'] = state_data['Confirmed'].map(int)
state_data['Recovered'] = state_data['Recovered'].map(int)
state_data['Deaths']  = state_data['Deaths'].map(int)

# pretty table representation
table = PrettyTable()
table.field_names = (new_cols)
for i in stats:
    table.add_row(i)
table.add_row(["","Total", 
               sum(state_data['Confirmed']), 
               sum(state_data['Recovered']), 
               sum(state_data['Deceased'])])
print(table)

# barplot to show total confirmed cases Statewise 
sns.set_style("checks")
plt.figure(figsize = (15,10))
plt.barh(state_data["States/UT"], state_data["Confirmed"].map(int),
         align = 'center', color = 'lightgreen', edgecolor = 'green')
plt.xlabel('No. of Confirmed cases', fontsize = 16)
plt.ylabel('States/UT', fontsize = 16)
