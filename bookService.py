from repository import Repository
from memberService import MemberService
from book import Book


class BookService():
    def get_booksList(self):
        print("\nLista de Personas")
        return Repository.booksList

    def createBook(self):
        name = input("\nIngrese el Titulo: ")
        authorName = input("Ingrese el Autor: ")
        memberLegajo = int(input("Ingrese el legajo: "))
        book = Book(name, authorName, memberLegajo)
        return book

    def add_book(self, book=None):
        print("\nAgregar Libro")
        if book is None:
            book = self.createBook()
        key = len(Repository.booksList)
        Repository.booksList[key] = book.__dict__

        print("\n¡%s añadido exitosamente!" % (book.name))

    def update_book(self, key=None, opc=None):
        print("\nActualizar Libro")

        if key is None:
            key = int(input("\nIngrese el ID del Libro: "))
        book = Repository.booksList[key]
        print("\nLibro: %s" % book)
        print("\n1. Titulo")
        print("2. Autor")
        print("3. Miembro")

        if opc is None:
            opc = int(input("\nIngrese el atributo que desea modificar: "))
        modify = input("\nIngrese el nuevo valor: ")
        if opc == 1:
            book['_name'] = modify.upper()
        if opc == 2:
            book['_authorName'] = modify.upper()
        if opc == 3:
            book['_memberLegajo'] = int(modify)

        print("\n¡Modificacion exitosa!\n%s" % book)

    def assign_book(self, book_id, legajo):
        self.book_id = BookService().add_book(book_id)
        self._legajo = MemberService().add_member(legajo)
        return book_id, legajo

    def delete_book(self):
        k = input("\nIngrese el codigo del Libro: ")
        print(self.repository.booksList[k])
        yn = input("\n¿Seguro que desea eliminar este registro? Y/N\n")
        if yn.upper() == "Y":
            del self.repository.booksList[k]
            print("Registro eliminado!")
