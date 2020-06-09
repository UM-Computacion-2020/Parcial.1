class Book():
    def __init__(self, name="", authorName="", memberLegajo=None):
        self._name = name.upper()
        self._authorName = authorName.upper()
        self._memberLegajo = memberLegajo

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def authorName(self):
        return self._authorName

    @authorName.setter
    def authorName(self, authorName):
        self._authorName = authorName.upper()

    @property
    def memberLegajo(self):
        return self._memberLegajo

    @memberLegajo.setter
    def memberLegajo(self, memberLegajo):
        self.memberLegajo = memberLegajo


if __name__ == "__main__":
    libro1 = Book("Python", "Linux", 57059)
    print(Book.name, Book.authorName, Book.memberLegajo)
