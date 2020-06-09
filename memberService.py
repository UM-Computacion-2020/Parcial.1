from repository import Repository
from member import Member


class MemberService():
    def get_membersList(self):
        print("\nLista de Personas")
        return Repository.membersList

    def createMember(self):
        name = input("\nIngrese Nombre: ")
        surname = input("Ingrese Apellido: ")
        age = int(input("Ingrese Edad: "))
        celular = int(input("Ingrese Celular: "))
        member = Member(name, surname, age, celular)
        return member

    def add_member(self, member=None):
        print("\nAgregar Persona")
        if member is None:
            member = self.createMember()
        key = len(Repository.membersList)
        Repository.membersList[key] = member.__dict__

        print("\n¡%s %s añadido exitosamente!" % (member.name, member.surname))

    def update_member(self, key=None, opc=None):
        print("\nActualizar Persona")

        if key is None:
            key = int(input("\nIngrese el codigo de la persona: "))
        member = Repository.membersList[key]
        print("\nMiembro: %s" % member)
        print("\n1. Nombre")
        print("2. Apellido")
        print("3. Edad")
        print("4. Celular")

        if opc is None:
            opc = int(input("\nIngrese el atributo que desea modificar: "))
        modify = input("\nIngrese el nuevo valor: ")
        if opc == 1:
            member['_name'] = modify.upper()
        if opc == 2:
            member['_surname'] = modify.upper()
        if opc == 3:
            member['_age'] = int(modify)
        if opc == 4:
            member['_celular'] = int(modify)

        print("\n¡Modificacion exitosa!\n%s" % member)
