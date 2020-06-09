class Member:
    def __init__(self, _name='', _surname='', _age='', _phone=''):
        self._name = _name.upper()
        self._surname = _surname.upper()
        self._age = _age
        self._phone = _phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name.upper()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, _surname):
        self._surname = _surname.upper()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, _age):
        self._age = _age

    @property
    def phone(self):
        return self._phone

    @age.setter
    def phone(self, _phone):
        self._phone = _phone
