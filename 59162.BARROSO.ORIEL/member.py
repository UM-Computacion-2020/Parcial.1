class Member():
    def __init__(self, name="", surname="", age="", phone=""):
        self._name = name.upper()
        self._surname = surname.upper()
        self._age = age
        self._phone = phone

    @property
    def name(self):
        return (self._name.upper())

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return (self._surname.upper())

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def age(self):
        return (self._age)

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def phone(self):
        return (self._phone)

    @phone.setter
    def phone(self, value):
        self._phone = value
