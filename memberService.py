from repository import Repository


class MemberService:
    contador = 1

    def add_member(self, member):
        leg = MemberService.contador
        Repository.membersList[MemberService.contador] = member.__dict__
        MemberService.contador += 1
        return leg

    def delete_member(self, leg):
        if leg < MemberService.contador:
            Repository.membersList[leg] = None
        else:
            raise ValueError("El legajo no existe")

    def update_member(self, leg, member):
        try:
            if leg < MemberService.contador:
                Repository.membersList[leg] = member.__dict__
                return
            raise KeyError
        except KeyError:
            raise ValueError
