# Object Relations Code Challenge - Articles

For this assignment, you will be working with a Magazine domain.

We have three models: `Author`, `Article`, and `Magazine`.

For our purposes, an `Author` has many `Article`s, a `Magazine` has many `Article`s, and `Article`s belong to both `Author` and `Magazine`.

`Author` - `Magazine` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests. You can run `pytest` to see the test results.

We've also provided you with a tool that you can use to manually test your code. To use it, run `python tools/debug.py` from the command line. This will start a `ipdb` session with your classes defined. You can test out the methods that you write here. You can add code to the `tools/debug.py` file to define variables and create sample instances of your objects.

**Before you submit!** Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

### Initializers, Readers, and Writers

#### Author

- `Author __init__(self, name)`
  - Initializes an `Author` object with a name of type `str`.
- `Author property name`
  - The getter should return the name of the author.
  - The setter should validate that the name is greater than 0 characters.
    - `raise ValueError` if the validation fails.

#### Magazine

- `Magazine __init__(self, name, category)`
  - A magazine is initialized with a name (`str`) and a category (`str`)
- `Magazine property name`
  - The getter should return the name of the magazine.
  - The setter should validate that the name is greater than 0 characters.
    - `raise ValueError` if the validation fails.


#### Article

- `Article __init__(self, author, magazine, title, word_count)`
  - An article is initialized with an author (`Author`), a magazine as a (`Magazine`), and title (`str`) and a word_count (`int`).
  - When an article is initialized, it should append itself to the author's `articles` attribute.
  - When an article is initialized, it should append itself to the magazine's `articles` attribute.

- `Article property word_count`
  - The getter should return the word count.
  - The setter should validate that the word count is not negative
    - `raise ValueError` if the validation fails

### Object Relationship Methods

#### Article

- `.author`
  - Should return the `Author` object associated with this article. 
  - This can be a property but it's not required
- `.magazine`
  - Should return the `Magazine` object associated with this article.
  - This can be a property but it's not required

#### Author

- `.articles`
  - Returns an `list` of `Article` objects the author has written
  - This can be a property but it's not required
- `Author get_magazines()`
  - Returns all the `Magazine` objects that this author has written articles for
    - **hint**: You can access the magazines by looping over `.articles`
    - *stretch goal*: Only return unique magazines. 

#### Magazine

- `.articles`
  - Returns an `list` of `Article` objects that have been written for the magazine
  - This can be a property but it's not required
- `Magazine get_authors()`
  - Returns all the `Author` objects who have written for this magazine
    - **hint**: You can access the authors by looping over `.articles`
    - *stretch goal*: Only return unique authors.

### Associations and Aggregate Methods

#### Author
- `Author get_shortest_article()`
  - Returns the `Article` object with the smallest `word_count` written by this author

#### Magazine

- `Magazine get_article_titles()`
  - Returns an `list` of all the titles of all articles written for that magazine
  - Should return a list of title strings, *not* a list of Article objects.
- `Magazine get_longest_article()`
  - Returns the `Article` object for this magazine that has the largest `word_count`
- `Magazine get_average_word_count()`
  - Returns the average `word_count` for all articles in the magazine.
- `Magazine get_top_contributor()`
  - **This is an optional stretch goal!**
  - Returns the `Author` who wrote the most articles for the magazine.
  - Return the `Author` object, *not* the author's name
  - If there is more than one `Author` who wrote the most articles, return any one of them.
  - Uncomment lines 144-153 in `test_challenge.py` if you want to unit test this function.
