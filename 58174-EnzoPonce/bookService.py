from book import Book
from repository import Repository


class BookService():
    def get_book(self):
        return Repository.booksList

    def add_book(self, book= None):
        bookKey = -1
        for key in Repository.booksList:
            bookKey = key
        bookKey = bookKey + 1
        Repository.booksList[bookKey] = book.__dict__

    def update_book(self, key, book):
        Repository.booksList[key]['_name'] = book._name
        Repository.booksList[key]['_authorname'] = book._authorname
        Repository.booksList[key]['_memberLegajo'] = book._memberLegajo

    def delete_book(self, key):
        del Repository.booksList[key]
    pass


    