from repository import Repository
from book import Book


class BookService:

    def get_BookList(self):
        return Repository.booksList

    def add_book(self, lib=None):
        print("\n Agregando Libro")
        if lib is None:
            name = (input("Ingrese el nombre: "))
            authorName = (input("Ingrese el nombre del autor: "))
            memberLegajo = int(input("Ingrese su legajo: "))
            bookKey = int(input("Ingrese la key: "))

            lib = Book(name, authorName, memberLegajo, bookKey)
        print("\n Agregando libro: %s" % lib.name)

        Repository.booksList[lib.bookKey] = lib.__dict__

    def update_book(self):
        print("\n Updating book")
        bookKey = int(input("Ingrese la key del libro a actualizar"))
        lib = Repository.booksList[bookKey]
        print("Book %s" % lib)
        name = input("Ingrese el nombre: ")
        authorName = input("Ingrese el nombre del autor: ")
        memberLegajo = input("Ingrese su legajo: ")
        booksList = booksList (name, authorName, memberLegajo, bookKey)
        Repository.booksList[bookKey]
