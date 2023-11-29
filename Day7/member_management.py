class LibraryMember:
    def __init__(self, member_id, name, phone_no):
        self.member_id = member_id
        self.name = name
        self.phone_no = phone_no


members = {}


def add_member(member_id, name, phone_no):
    if member_id not in members:
        member = LibraryMember(member_id, name, phone_no)
        members[member_id] = member
    else:
        raise ValueError("Member id already exists.")


def update_member(member_id, name, phone_no):
    if member_id in members:
        members[member_id].name = name
        members[member_id].phone_no = phone_no
    else:
        raise ValueError("Member doesn't exists.")


def remove_member(member_id):
    if member_id in members:
        del members[member_id]
    else:
        raise ValueError("Member doesn't exists.")
