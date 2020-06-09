class Book():
    def __init__(self, name="", authorname="", memberLegajo=""):
        self._name = name.upper()
        self._authorname = authorname.upper()
        self._memberLegajo = memberLegajo

    @property
    def name(self):
        return (self._name)

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def authorname(self):
        return (self._authorname)

    @authorname.setter
    def authorname(self, value):
        self._authorname = value

    @property
    def memberLegajo(self):
        return (self._legajo)

    @memberLegajo.setter
    def memberLegajo(self, value):
        self._legajo = value
