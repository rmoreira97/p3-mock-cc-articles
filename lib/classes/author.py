class Author:
    def __init__(self, name):
        self._name = None
        self.name = name
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Author name must have at least one character")
        self._name = value

    def get_magazines(self):
        return list(set(article.magazine for article in self.articles))

    def has_written_for_magazine(self, magazine):
        return any(article.magazine == magazine for article in self.articles)
