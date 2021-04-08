import requests
from bs4 import BeautifulSoup

print("Importem llibreria request per demanar les dades")
print("importem la llibreria BeatifulSoup per llegir el contingut de les dades")
def readPage(page):
    res = []
    url = "https://www.meneame.net/?page={}".format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    for article in soup.find_all(attrs={'class': 'news-body'}):
        title = article.find('h2').a.string
        summary = article.find(attrs={'class': 'news-content'}).string
        extern_url = article.find('h2').a['href']
        votes = article.find(attrs={'class': 'votes'}).a.string
        date1_node = article.find('span', {'data-ts': True})
        published_date = date1_node['data-ts']
        if date1_node.find_next_sibling('span', {'data-ts': True}):
            send_date = date1_node.next_sibling.next_sibling['data-ts']
        else:
            send_date = '0'
        category = article.find(attrs={'class': 'subname'}).string
        res.append(Entry(page, extern_url, title,
                   summary, votes, published_date, send_date, category))
    return res

print("Creem una funció que vagi llegin les pàgines que demanem i aconseguim els continguts de: page, url, title, summary, votes, published_date, send_date, category")

class Entry:
    def __init__(self, page, url, title, summary, votes, published_date, send_date, category):
        self.page = page
        self.url = url
        self.title = title
        self.summary = summary
        self.votes = votes
        self.published_date = published_date
        self.send_date = send_date
        self.category= category
        
print("Vinculem els atributs amb els arguments que l'hi hem donat")