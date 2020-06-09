from repository import Repository
from member import Member


class MemberService:

    def get_MemberList(self):
        return Repository().membersList

    # Agrega una persona en el dicionario person, definido en Repository
    def add_member(self, member):
        key = -1
        for lastkey in Repository.membersList:
            key = lastkey
        key = key + 1
        Repository.membersList[key] = member.__dict__
        return key

    def update_member(self, legajo, member):
        Repository.membersList[legajo] = member.__dict__

    def delete_member(self, legajo):
        del(Repository.membersList[legajo])

    def delete_member_value_error_legajo(self, legajo):
        try:
            del(Repository.membersList[legajo])
        except ValueError:
            pass
