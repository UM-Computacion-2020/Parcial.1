from repository import Repository


class BookService:
    contador = 1

    def add_book(self, book):
        idBook = BookService.contador
        Repository.booksList[BookService.contador] = book.__dict__
        BookService.contador += 1
        return idBook

    def update_book(self, idBook, member):
        try:
            if idBook < BookService.contador:
                Repository.membersList[idBook] = member.__dict__
                return
            raise KeyError
        except KeyError:
            raise ValueError
