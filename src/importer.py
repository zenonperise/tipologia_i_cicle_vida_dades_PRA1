def readPage(page):
    res = []
    res.append(Entry(page))
    res.append(Entry(page))
    return res


class Entry:
    def __init__(self, page):
        self.page = page
        # Other attributes here
