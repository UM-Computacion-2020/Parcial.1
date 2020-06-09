from repository import Repository


class BookService():
    def get_book(self):
        return Repository.booksList

    def add_book(self, book):
        lkey = -1
        for key in Repository.booksList:
            lkey = key
        lkey = lkey + 1
        Repository.booksList[lkey] = (book._name, book._authorname,
                                      book._legajo)

    def update_book(self, key, book):
        key = len(Repository.booksList)
        Repository.booksList[key] = (book._name, book._authorname,
                                     book._legajo)

    def delete_book(self, key):
        del Repository.booksList[key]
