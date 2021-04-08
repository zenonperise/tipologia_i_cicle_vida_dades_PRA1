from pandas import DataFrame
import time


print("Importem llibreria pandas per carragar les variables")
print("Importem llibreria time per afegir delay i per obtenir dades sense saturar el servidor)
pages = 600
allData = []
for page in range(pages):
    time.sleep(1)
    for entry in readPage(page):
        allData.append(entry)
       
page = list(map(lambda x: x.page, allData))
url = list(map(lambda x: x.url, allData))
summary = list(map(lambda x: x.summary, allData))
votes = list(map(lambda x: x.votes, allData))
published_date = list(map(lambda x: x.date1, allData))
send_date = list(map(lambda x: x.date2, allData))
category = list(map(lambda x: x.category, allData))

data = [page, url, summary, votes, published_date, send_date, category]

df = DataFrame(data).transpose()

df.columns = ["page", "url", "summary", "votes", "published_date", "send_date", "category"]

print("Variables carregades i amb encapçalat")
