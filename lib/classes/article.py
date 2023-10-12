class Article:
    def __init__(self, author, magazine, title, word_count):
        self.author = author
        self.magazine = magazine
        self.title = title
        self._word_count = None
        self.word_count = word_count  # Using the setter method to validate and set word_count
        author.articles.append(self)
        magazine.articles.append(self)

    @property
    def word_count(self):
        return self._word_count

    @word_count.setter
    def word_count(self, value):
        if value < 0:
            raise ValueError("Word count cannot be negative")
        self._word_count = value
