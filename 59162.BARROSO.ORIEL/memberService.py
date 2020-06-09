from repository import Repository


class MemberService():

    def get_member(self):
        return Repository.membersList

    def add_member(self, member):
        memberKey = -1
        for key in Repository.membersList:
            memberKey = key
        memberKey = memberKey + 1
        Repository.membersList[memberKey] = (member._name, member._surname,
                                             member._age, member._phone)

    def update_member(self, legajo, member):
        legajo = len(Repository.membersList)
        Repository.membersList[legajo] = (member._name, member._surname,
                                          member._age, member._phone)

    def delete_member(self, key):
        del Repository.membersList[key]
