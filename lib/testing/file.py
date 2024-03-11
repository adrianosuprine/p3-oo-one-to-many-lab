class Article:
#     #class variable to store magazines
#     all = []

#     #Initilaize magazine instance

#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self._title = str(title)  
#         #add the titles to the mpty list
#         Article.all.append(self)

# #getter method for title
#     @property
#     def title(self):
#         return self._title
    
# #setter method for the title
#     @title.setter
#     def title(self, new_title):
#         return self._title


# #initialize the author with a name
# class Author:
#     #private attribute of name
#     def __init__(self, name):
#         self._name = name

#      #getter method for name   
#     @property
#     def name(self):
#         return self._name
#     # setter method for name
#     @name.setter
#     def name(self, new_name):
#         self.new_name = new_name
#         return self._name
    
#     #get articles written by the author
#     def articles(self):
#         return [article for article in Article.all if article.author == self]
   
#     #get the magazines the authour has contributed to
#     def magazines(self):
#         return list(set([article.magazine for article in self.articles()]))

#     #add an article written by the auothor
#     def add_article(self, magazine, title):
#         article = Article(self, magazine, title)
#         return article

#      # get the topics authour has contributed to
#     def topic_areas(self):
#         return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None
   
#     # method to get contributing authors
#     def contributing_authors(self):
#         return [author for author in Author.all if len(author.articles()) > 0]

# #initialize magazine with name and category
# class Magazine:
#     def __init__(self, name, category):
#         self._name = name
#         self._category = category
# # getter method for name 
#     @property
#     def name(self):
#         return self._name
# #setter for category
#     @property
#     def category(self):
#         return self._category
#    #setter method for name 
#     @name.setter
#     def name(self,new_name):
#         if isinstance (new_name,str):
#             if len(new_name)>=2 and len(new_name) <=16:
#                 self._name = new_name
#         return self._name
    
#     # setter method for category
#     @category.setter
#     def category(self,new_category):
#         if isinstance (new_category,str):
#             if len(new_category) > 0:
#                 self._category = new_category
#         return self._name
    
#     #method to retrive articles
#     def articles(self):
#         return [article for article in Article.all if article.magazine == self]

#     #method to get the contributors of a magazine
#     def contributors(self):
#         return list(set([article.author for article in self.articles()]))
    
#     # method to get the titles of articles
#     def article_titles(self):
#         titles = [article.title for article in self.articles()]
#         return titles if titles else None

# #method to get authors who contributed more than 2 articles
#     def contributing_authors(self):
#         authors = {}
#         for article in self.articles():
#             if article.author in authors:
#                 authors[article.author] += 1
#             else:
#                 authors[article.author] = 1
#         contributing_authors = [author for author, count in authors.items() if count > 2]
#         return contributing_authors if contributing_authors else None


# gpt
# class Article:
#     def __init__(self, author, magazine, title):
#         self._title = title
#         self._author = author
#         self._magazine = magazine

#     @property
#     def title(self):
#         return self._title

#     @property
#     def author(self):
#         return self._author

#     @property
#     def magazine(self):
#         return self._magazine
   
# class Author:
#     def __init__(self, name):
#         if not isinstance(name, str) or len(name) == 0:
#             raise ValueError("Name must be a non-empty string")
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     def add_article(self, magazine, title):
#         article = Article(self, magazine, title)
#         return article

#     def topic_areas(self):
#         articles = self.articles()
#         if not articles:
#             return None
#         return list(set([article.magazine.category for article in articles]))


# class Magazine:
#     def __init__(self, name, category):
#         if not isinstance(name, str) or not (2 <= len(name) <= 16):
#             raise ValueError("Name must be a string between 2 and 16 characters")
#         if not isinstance(category, str) or len(category) == 0:
#             raise ValueError("Category must be a non-empty string")
#         self._name = name
#         self._category = category

#     @property
#     def name(self):
#         return self._name

#     @property
#     def category(self):
#         return self._category
#     def article_titles(self):
#         articles = self.articles()
#         if not articles:
#             return None
#         return [article.title for article in articles]

#     def contributing_authors(self):
#         authors_count = {}
#         for article in self.articles():
#             author = article.author
#             authors_count[author] = authors_count.get(author, 0) + 1

#         return [author for author, count in authors_count.items() if count > 2] if authors_count else None

#     @classmethod
#     def top_publisher(cls):
#         magazines = cls.all()
#         if not magazines:
#             return None
#         return max(magazines, key=lambda magazine: len(magazine.articles()))