class Magazine:
    def __init__(self, name, category):
        self._name = None
        self.name = name
        self._category = None
        self.category = category
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Magazine name must have at least one character")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) == 0:
            raise ValueError("Magazine category must have at least one character")
        self._category = value

    def get_authors(self):
        return list(set(article.author for article in self.articles))

    def get_article_titles(self):
        return [article.title for article in self.articles]

    def get_longest_article(self):
        return max(self.articles, key=lambda article: article.word_count, default=None)

    def get_average_word_count(self):
        if not self.articles:
            return 0
        total_word_count = sum(article.word_count for article in self.articles)
        return total_word_count / len(self.articles)

    def get_top_contributor(self):
        author_counts = {}
        for article in self.articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        top_author = max(author_counts, key=author_counts.get, default=None)
        return top_author
