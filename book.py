class Book():
    def __init__(self, name="None", authorName="None", memberLegajo=None):
        self.name = name
        self.author = authorName
        self.memberLegajo = memberLegajo


@property
def name(self):
    return self.name


@name.setter
def name(self, name):
    self.name = name


@property
def authorName(self):
    return self.authorName


@authorName.setter
def authorName(self, authorName):
    self.authorName = authorName


@property
def memberLegajo(self):
    return self.memberLegajo


@memberLegajo.setter
def memberLegajo(self, memberLegajo):
    self.memberLegajo = memberLegajo


def _str_(self):
    "(%s, %s, %d)" % (self.name, self.authorName, self.memberLegajo)
