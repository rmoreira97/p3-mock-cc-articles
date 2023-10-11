class Article:
    def __init__(self, author, magazine, title, word_count):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.word_count = word_count
        author.articles.append(self)
        magazine.articles.append(self)
