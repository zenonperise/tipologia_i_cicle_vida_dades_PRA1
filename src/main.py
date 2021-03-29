
from importer import readPage

pages = 1
allData = []
for page in range(pages):
    for entry in readPage(page):
        allData.append(entry)

print(list(map(lambda x: x.url, allData)))
