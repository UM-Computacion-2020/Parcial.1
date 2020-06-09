class Member():
    def __init__(self, name="", surname="", age=None, celular=None):
        self._name = name.upper()
        self._surname = surname.upper()
        self._age = age
        self._celular = celular

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname.upper()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self.age = age

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, celular):
        self.celular = celular


if __name__ == "__main__":
    miembro1 = Member("Gabriel", "Sosa", 2634213316, 57059)
    print(Member.name, Member.surname, Member.age, Member.celular)
