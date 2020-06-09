from repository import Repository
from member import Member


class MemberService:

    def get_memberList(self):
        return Repository.membersList

    def add_member(self, mem=None):
        print("\n Agregando Miembro")
        if mem is None:
            name = (input("Ingrese el nombre: "))
            surname = (input("Ingrese su apellido: "))
            age = int(input("Ingrese su edad: "))
            phone = int(input("Ingrese su celular: "))
            legajo = int(input("Ingrese el legajo"))
            memberKey = int(input("Ingrese la key: "))

            mem = miembro(name, surname, age, phone, legajo, memberKey)
        print("\n Agregando miembro: %s" % mem.name)

        Repository.membersList[mem.memberKey] = mem.__dict__

    def update_member(self):
        print("\n Updating member")
        memberKey = int(input("Ingrese la key del miembro a actualizar"))
        lib = Repository.membersList[memberKey]
        print("Member %s" % mem)
        name = input("Ingrese el nombre: ")
        surname = input("Ingrese el apellido: ")
        age = int(input("Ingrese la edad: ")
        phone = int(input("Ingrese el número: "))
        legajo = int(input("Ingrese el legajo: "))
        membersList = membersList (name, surname, age, phone, legajo, memberKey)
        Repository.membersList[memberKey]

    def delete_member(self, memberKey):
        print("\n   Eliminando miembro")
        memberKey = int(input("Ingrese la key del miembro a eliminar"))
        del self.Repository.membersList[memberKey]
