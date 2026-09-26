

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://tgftp.nws.noaa.gov/weather/current/HECA.html"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

title = soup.find("b").get_text(strip=True)
print("\n","Title:", title,"\n")

records = []
rows = soup.find_all("tr")

for row in rows:
    cells = row.find_all("td")
    data = []
    for cell in cells:
        data.append(cell.get_text(" ", strip=True))
    if len(data) == 7 and data[1] not in ["Time EDT (UTC)"]:
        records.append({
            "Time": data[1],
            "Temperature": data[2],
            "Dew Point": data[3],
            "Pressure": data[4],
            "Wind": data[5],
            "Weather": data[6]})
df = pd.DataFrame(records)
print(df)

'''
output:
Title: Current Weather Conditions:Cairo Airport, Egypt 

                   Time Temperature Dew Point      Pressure    Wind Weather
0      7 AM (11) Sep 26     82 (28)   53 (12)  29.94 (1014)     N 8        
1      6 AM (10) Sep 26     82 (28)   53 (12)  29.94 (1014)   NNW 7        
2       5 AM (9) Sep 26     80 (27)   53 (12)  29.97 (1015)   ENE 5        
3       4 AM (8) Sep 26     78 (26)   55 (13)  29.97 (1015)     N 7        
4       3 AM (7) Sep 26     77 (25)   57 (14)  29.97 (1015)     N 6        
5       2 AM (6) Sep 26     73 (23)   57 (14)  29.97 (1015)     N 7        
6       1 AM (5) Sep 26     73 (23)   55 (13)  29.97 (1015)   ENE 3        
7   Midnight (4) Sep 26     69 (21)   55 (13)  29.97 (1015)   ENE 2        
8      11 PM (3) Sep 25     69 (21)   55 (13)  29.94 (1014)     E 7        
9      10 PM (2) Sep 25     69 (21)   55 (13)  29.97 (1015)   ENE 3        
10      9 PM (1) Sep 25     69 (21)   55 (13)  29.97 (1015)   ENE 3        
11      8 PM (0) Sep 25     71 (22)   57 (14)  29.97 (1015)   NNE 7        
12     7 PM (23) Sep 25     71 (22)   57 (14)  30.00 (1016)    N 12        
13     6 PM (22) Sep 25     73 (23)   57 (14)  30.00 (1016)    N 12        
14     5 PM (21) Sep 25     73 (23)   57 (14)  30.03 (1017)    N 12        
15     4 PM (20) Sep 25     73 (23)   57 (14)  30.03 (1017)    N 13        
16     3 PM (19) Sep 25     75 (24)   57 (14)  30.03 (1017)    N 15        
17     2 PM (18) Sep 25     77 (25)   55 (13)  30.03 (1017)    N 17        
18     1 PM (17) Sep 25     78 (26)   59 (15)  30.00 (1016)    N 21        
19     Noon (16) Sep 25     80 (27)   60 (16)  29.97 (1015)  NNW 17        
20    11 AM (15) Sep 25     84 (29)   57 (14)  29.97 (1015)    N 15        
21    10 AM (14) Sep 25     86 (30)   57 (14)  29.94 (1014)    N 10        
22     9 AM (13) Sep 25     86 (30)   57 (14)  29.94 (1014)    N 10        
23     8 AM (12) Sep 25     86 (30)   59 (15)  29.94 (1014)    N 10        

Process finished with exit code 0'''