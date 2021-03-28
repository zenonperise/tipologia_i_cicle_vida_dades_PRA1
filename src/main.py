
from importer import readPage

pages = 10
allData = []
for page in range(pages):
    for entry in readPage(page):
        allData.append(entry)

print((allData))
