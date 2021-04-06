
from importer import readPage
from pandas import DataFrame
import time
import csv

pages = 3
allData = []
for page in range(pages):
    time.sleep(20)
    for entry in readPage(page):
        allData.append(entry)
       
page = list(map(lambda x: x.page, allData))
url = list(map(lambda x: x.url, allData))
summary = list(map(lambda x: x.summary, allData))
votes = list(map(lambda x: x.votes, allData))
date1 = list(map(lambda x: x.date1, allData))
date2 = list(map(lambda x: x.date2, allData))
category = list(map(lambda x: x.category, allData))

data = [page, url, summary, votes, date1, date2, category]

df = DataFrame(data).transpose()

df.columns = ["page", "url", "summary", "votes", "date1", "date2", "category"]

df= df.to_csv(index=False)
with open('output.csv', 'w+') as f:
    f.write(df)