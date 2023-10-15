
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

"""
    + id: Int
    + first_name: String
    + last_name: String (Always Jackson)
    + age: Int > 0
    + lucky_numbers: Array of int
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"id": 1, "first_name": "John", "last_name": self.last_name, "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "last_name": self.last_name, "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "last_name": self.last_name, "age": 5, "lucky_numbers": [1]},
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member.get("id") is None:
            member["id"] = self._generateId()

        member["last_name"] = self.last_name
        
        self._members.append(member)

    def delete_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                del self._members[i]
                break

    def update_member(self, id, member):
        member["id"] = id
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                self._members[i] = member
                break

    def get_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                return self._members[i]
        
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
