import requests
import pandas as pd

www = requests.get('http://www.beje.pl/python/index.htm')

print(www.text)

df = pd.read_html(www)

table = pd.DataFrame(www).T
print(table)



from bs4 import BeautifulSoup

soup = BeautifulSoup(data, 'html.parser') # data is your table from question

rows = []
for tr in soup.select('tr'):
    rows.append([td.get_text(strip=True) for td in tr.select('th, td')])