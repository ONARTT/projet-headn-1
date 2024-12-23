import itertools

class Etudiant:
    newid = itertools.count()
    def __init__(self, name, age):
        self.id = next(Etudiant.newid)
        self.name = name
        self.age = age
        self.notes = []



    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.name,
            "age": self.age,
            "notes": self.notes,
            "moyenne": self.calc_moyenne()
        }

    def addNote(self, note):
        return self.notes.append(note)


    def calc_moyenne(self):
        if self.notes:
            return round(sum(self.notes) / len(self.notes),1)
        return 0

        
    def setName(self, name):
        self.name = name
        return

    def setAge(self, age):
        self.age = age
        return