class Boock:
    def __init__(self, _name='', _authorName='', _memberLegajo=''):
        self._name = _name.upper()
        self._authorName = _authorName.upper()
        self._memberLegajo = _memberLegajo

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name.upper()

    @property
    def authorName(self):
        return self._authorName

    @authorName.setter
    def authorName(self, _authorName):
        self._authorName = _authorName.upper()

    @property
    def memberLegajo(self):
        return self._memberLegajo

    @memberLegajo.setter
    def memberLegajo(self, _authorName):
        self._memberLegajo= _memberLegajo
