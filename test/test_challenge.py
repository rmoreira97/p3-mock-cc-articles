from lib.classes.author import Author
from lib.classes.article import Article
from lib.classes.magazine import Magazine
import pytest

def test_init_author_with_name():
    """Should be able to initialize an Author with a name."""
    author = Author('Joe')
    assert author.name == 'Joe'

def test_author_name_gt_0_chars():
    """Should raise Exception if author's name has no characters"""
    author = Author('Joe')
    assert author.name == 'Joe'  # valid name

    with pytest.raises(Exception):
        author.name = ''  # invalid name

def test_init_magazine_with_name_cateogry():
    """Should be able to initialize a Magazine with a name and category"""
    magazine = Magazine('Cosmo', 'fashion')
    assert magazine.name == 'Cosmo'
    assert magazine.category == 'fashion'

def test_magazine_name_gt_0_chars():
    """Should raise Exception if magazine's name is 0 chars"""
    zine = Magazine('Cosmo', 'fashion')
    assert zine.name == 'Cosmo'  # valid name

    with pytest.raises(Exception):
        zine.name = ''  # invalid name

def test_init_article_with_author_mag_title_word_count():
    """
    Should be able to initialize an Article with an author, magazine, and title.
    Initializing an Article should append itself to the author and magazine.
    """
    author = Author('Joe')
    zine = Magazine('Cosmo', 'fashion')
    article = Article(author, zine, '2023 Tennis Outfits', 250)

    assert article.author == author
    assert article.magazine == zine
    assert article.title == '2023 Tennis Outfits'
    assert article.word_count == 250

    assert len(author.articles) == 1
    assert author.articles[0] == article
    assert len(zine.articles) == 1
    assert zine.articles[0] == article

def test_article_word_count_is_not_negative():
    """Should raise Exception if the word_count is negative"""
    author = Author('Joe')
    zine = Magazine('Cosmo', 'fashion')

    with pytest.raises(Exception):
        Article(author, zine, '2023 Tennis Outfits', -1)

def test_author_has_articles():
    """Author should be able to access articles with .articles"""
    author = Author('Joe')
    zine = Magazine('Cosmo', 'fashion')
    article = Article(author, zine, '2023 Tennis Outfits', 250)

    assert len(author.articles) == 1
    assert author.articles[0] == article

def test_author_get_magazines():
    """
    .get_magazines() should return all the Magazine objects the 
    author has written articles for.
    """
    author = Author('Joe')
    cosmo = Magazine('Cosmo', 'fashion')
    vogue = Magazine('Vogue', 'fashion')
    Article(author, cosmo, '2023 Tennis Outfits', 250)

    assert cosmo in author.get_magazines()
    assert vogue not in author.get_magazines()

def test_magazine_has_articles():
    """Magazine should be able to access articles with .articles"""
    author = Author('Joe')
    zine = Magazine('Cosmo', 'fashion')
    article = Article(author, zine, '2023 Tennis Outfits', 250)
    
    assert len(zine.articles) == 1
    assert zine.articles[0] == article

def test_magazine_get_authors():
    """
    .get_authors() should return all the Author objects who 
    have written articles for the magazine.
    """
    joe = Author('Joe')
    anne = Author('Anne')
    cosmo = Magazine('Cosmo', 'fashion')
    Article(joe, cosmo, '2023 Tennis Outfits', 250)

    assert joe in cosmo.get_authors()
    assert anne not in cosmo.get_authors()

def test_author_has_written_for_magazine():
    """
    Should return True if the author has written an
    article for the given magazine, False otherwise
    """
    anne = Author('Anne')
    cosmo = Magazine('Cosmo', 'fashion')
    vogue = Magazine('Vogue', 'fashion')
    Article(anne, cosmo, '2023 Tennis Outfits', 250)

    assert anne.has_written_for_magazine(cosmo) == True
    assert anne.has_written_for_magazine(vogue) == False


def test_magazine_get_article_titles():
    anne = Author('Anne')
    cosmo = Magazine('Cosmo', 'fashion')
    Article(anne, cosmo, '2023 Tennis Outfits', 250)
    
    assert cosmo.get_article_titles() == ['2023 Tennis Outfits']

    Article(anne, cosmo, 'Best iPad Deals', 500)
    assert cosmo.get_article_titles() == ['2023 Tennis Outfits', 'Best iPad Deals']

def test_magazine_get_longest_article():
    """Should return the Article object with the largest word_count"""
    anne = Author('Anne')
    cosmo = Magazine('Cosmo', 'fashion')
    a1 = Article(anne, cosmo, 'Eight Hours With Lindsay Lohan', 12000)
    a2 = Article(anne, cosmo, '2023 Tennis Outfits', 250)
    a3 = Article(anne, cosmo, 'Best iPad Deals', 500)

    assert cosmo.get_longest_article() == a1

def test_magazine_get_average_word_count():
    """Should return the average word_count for all articles in this magazine"""
    anne = Author('Anne')
    cosmo = Magazine('Cosmo', 'fashion')
    a1 = Article(anne, cosmo, 'Eight Hours With Lindsay Lohan', 12000)
    a2 = Article(anne, cosmo, '2023 Tennis Outfits', 250)
    a3 = Article(anne, cosmo, 'Best iPad Deals', 500)

    assert cosmo.get_average_word_count() == 4250

# def test_magazine_get_top_contributor():
#     joe = Author('Joe')
#     anne = Author('Anne')
#     cosmo = Magazine('Cosmo', 'fashion')
#     # joe has written one article, anne has written two
#     Article(joe, cosmo, 'Eight Hours With Lindsay Lohan', 12000)
#     Article(anne, cosmo, '2023 Tennis Outfits', 250)
#     Article(anne, cosmo, 'Best iPad Deals', 500)

#     assert cosmo.get_top_contributor() == anne