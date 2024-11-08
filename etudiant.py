import itertools

class Etudiant:
    newid = itertools.count()
    def __init__(self, name, age):
        self.id = next(Etudiant.newid)
        self.name = name
        self.age = age



    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }