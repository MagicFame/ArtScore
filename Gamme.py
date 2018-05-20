class Gamme:

    # Constructeur
    def __init__(self, nom, note):
        self.nom = nom
        self.notes = list(note)

    # Retourne le nom de la gamme
    def getNom(self):
        return self.nom

    # Retourne les notes de la gamme
    def getNotes(self):
        return self.notes
