
from pandas import DataFrame
import time
from exporter import writeResult
from importer import readPage

print("Importem llibreria pandas per carregar les variables")
print("Importem llibreria time per afegir delay i per obtenir dades sense saturar el servidor")
pages = 600
allData = []
for page in range(pages):
    time.sleep(1)
    print("Llegint pàgina {}".format(page))
    for entry in readPage(page):
        allData.append(entry)

page = list(map(lambda x: x.page, allData))
url = list(map(lambda x: x.url, allData))
title = list(map(lambda x: x.title, allData))
summary = list(map(lambda x: x.summary, allData))
votes = list(map(lambda x: x.votes, allData))
published_date = list(map(lambda x: x.published_date, allData))
send_date = list(map(lambda x: x.send_date, allData))
category = list(map(lambda x: x.category, allData))

data = [page, url, title, summary, votes, published_date, send_date, category]

df = DataFrame(data).transpose()

df.columns = ["page", "url", "title", "summary", "votes",
              "published_date", "send_date", "category"]

print("Variables carregades i amb encapçalat")

writeResult(df)
