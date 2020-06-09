class Member():
    def __init__(self, name="None", surname="None", age=None, Phone="None", legajo=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.legajo = legajo


@property
def name(self):
    return self.name


@name.setter
def name(self, name):
    self.name = name


@property
def surname(self):
    return self.surname


@surname.setter
def surname(self, surname):
    self.surname = surname


@property
def age(self):
    return self.age


@age.setter
def age(self, age):
    self.age = age


@property
def phone(self):
    return self.phone


@phone.setter
def phone(self, phone):
    self.phone = phone


@property
def legajo(self, legajo):
    return self.legajo


@legajo.setter
def legajo(self, legajo):
    if legajo < 0:
        raise ValueError("No existe el legajo")
    self.legajo = legajo


def _str_(self):
    "(%s, %s, %d, %d, %d)" % (self.name, self.surname, self.age, self.phone, self.legajo)
