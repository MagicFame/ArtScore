class Gamme:
    nom = ""
    notes = []
    def __init__(self, nom, note):
        self.nom = nom
        self.notes = list(note)

    def getNom(self):
        return self.nom
    def getNotes(self): #Retourne les notes de la gamme
        return self.notes
