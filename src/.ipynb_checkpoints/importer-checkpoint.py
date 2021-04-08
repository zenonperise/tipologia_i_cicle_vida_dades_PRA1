import requests

from bs4 import BeautifulSoup


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
        date1 = date1_node['data-ts']
        if date1_node.find_next_sibling('span', {'data-ts': True}):
            date2 = date1_node.next_sibling.next_sibling['data-ts']
        else:
            date2 = '0'
        category = article.find(attrs={'class': 'subname'}).string
        res.append(Entry(page, extern_url, title,
                   summary, votes, date1, date2, category))
    return res


class Entry:
    def __init__(self, page, url, title, summary, votes, date1, date2, category):
        self.page = page
        self.url = url
        self.title = title
        self.summary = summary
        self.votes = votes
        self.date1 = date1
        self.date2 = date2
        self.category= category
        
        