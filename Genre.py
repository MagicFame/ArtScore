class Genre:  # def
    repartitionDoMajeur = 0
    repartitionDoMineur = 0
    repartitionLaMineur = 0
    repartitionSolMajeur = 0
    repartitionMiMineur = 0
    repartitionReMajeur = 0
    repartitionSiMineur = 0
    repartitionLaMajeur = 0
    repartitionFaDMineur = 0
    repartitionMiMajeur = 0
    repartitionDoDMineur = 0
    repartitionSiMajeur = 0
    repartitionSolDMineur = 0
    repartitionFaDMajeur = 0
    repartitionReDMineur = 0
    repartitionDoDMajeur = 0
    repartitionLaDMineur = 0
    repartitionFaMajeur = 0
    repartitionReMineur = 0
    repartitionLaDMajeur = 0
    repartitionSolMineur = 0
    repartitionReDMajeur = 0
    repartitionSolDMajeur = 0
    repartitionFaMineur = 0

    dissonnaceTotale = 0
    repartitionTotale = 0

    def __init__(self, nom):  # constructeur
        self.nom = nom
        self.notes = []
        self.gam = ""

    def addGamme(self, nom):
        if nom == "Do majeur":
            self.repartitionDoMajeur = self.repartitionDoMajeur + 1
        if nom == "La mineur":
            self.repartitionLaMineur = self.repartitionLaMineur + 1
        if nom == "Sol majeur":
            self.repartitionSolMajeur = self.repartitionSolMajeur + 1
        if nom == "Mi mineur":
            self.repartitionMiMineur = self.repartitionMiMineur + 1
        if nom == "Re majeur":
            self.repartitionReMajeur = self.repartitionReMajeur + 1
        if nom == "Si mineur":
            self.repartitionSiMineur = self.repartitionSiMineur + 1
        if nom == "La majeur":
            self.repartitionLaMajeur = self.repartitionLaMajeur + 1
        if nom == "Fa# mineur":
            self.repartitionFaDMineur = self.repartitionFaDMineur + 1
        if nom == "Mi majeur":
            self.repartitionMiMajeur = self.repartitionMiMajeur + 1
        if nom == "Do# mineur":
            self.repartitionDoDMineur = self.repartitionDoDMineur + 1
        if nom == "Si majeur":
            self.repartitionSiMajeur = self.repartitionSiMajeur + 1
        if nom == "Sol# mineur":
            self.repartitionSolDMineur = self.repartitionSolDMineur + 1
        if nom == "Fa# majeur":
            self.repartitionFaDMajeur = self.repartitionFaDMajeur + 1
        if nom == "Re# mineur":
            self.repartitionReDMineur = self.repartitionReDMineur + 1
        if nom == "Do# majeur":
            self.repartitionDoDMajeur = self.repartitionDoDMajeur + 1
        if nom == "La# mineur":
            self.repartitionLaDMineur = self.repartitionLaDMineur + 1
        if nom == "Fa majeur":
            self.repartitionFaMajeur = self.repartitionFaMajeur + 1
        if nom == "Re mineur":
            self.repartitionReMineur = self.repartitionReMineur + 1
        if nom == "La# majeur":
            self.repartitionLaDMajeur = self.repartitionLaDMajeur + 1
        if nom == "Sol mineur":
            self.repartitionSolMineur = self.repartitionSolMineur + 1
        if nom == "Re# majeur":
            self.repartitionReDMajeur = self.repartitionReDMajeur + 1
        if nom == "Do mineur":
            self.repartitionDoDMineur = self.repartitionDoDMineur + 1
        if nom == "Sol# majeur":
            self.repartitionSolDMajeur = self.repartitionSolDMajeur + 1
        if nom == "Fa mineur":
            self.repartitionFaMineur = self.repartitionFaMineur + 1

    def addDissonance(self, value):
        self.dissonnaceTotale += value

    def addRepartition(self, value):
        self.repartitionTotale += value

    def afficherInfoGenre(self):
        print("\n \n \n \nStyle selectionné : Classique")
        print("Gamme répartition Do majeur : ", self.repartitionDoMajeur, "Do mineur : ", self.repartitionDoMineur,
              "La mineur: ", self.repartitionLaMineur, "Sol majeur: ", self.repartitionSolMajeur, "Mi mineur:",
              self.repartitionMiMineur, "Re majeur : ", self.repartitionReMajeur, "Si mineur", self.repartitionSiMineur,
              "La majeur : ", self.repartitionLaMajeur, "Fa# mineur: ", self.repartitionFaDMineur,
              "Mi majeur: ", self.repartitionMiMajeur, "Do# mineur:", self.repartitionDoDMineur, "Si majeur : ",
              self.repartitionSiMajeur, "Sol# mineur", self.repartitionSolDMineur, "Fa# majeur : ",
              self.repartitionFaDMajeur, "\nRe# mineur  : ", self.repartitionReDMineur, "Do# majeur: ",
              self.repartitionDoDMajeur,
              "La# mineur: ", self.repartitionLaDMineur, "Fa majeur:", self.repartitionFaMajeur, "Re mineur : ",
              self.repartitionReMineur, "La# majeur", self.repartitionLaDMajeur,
              "Sol mineur : ", self.repartitionSolMineur, "Re# majeur", self.repartitionReDMajeur, "Sol# majeur",
              self.repartitionSolDMajeur, "Fa mineur", self.repartitionFaMineur)
        print("\nDissonnance moyenne :", self.dissonnaceTotale / 360)
        print("\nRepartition moyenne", self.repartitionTotale / 360)

    def chooseGenre(self):  # A adapter par rapport aux pourcentages
        total = self.repartitionDoMajeur + self.repartitionDoMineur + self.repartitionLaMineur + \
                self.repartitionSolMajeur + self.repartitionMiMineur + self.repartitionReMajeur + \
                self.repartitionSiMineur + self.repartitionLaMajeur + self.repartitionFaDMineur + \
                self.repartitionMiMajeur + self.repartitionDoDMineur + self.repartitionSiMajeur + \
                self.repartitionSolDMineur + self.repartitionFaDMajeur + self.repartitionReDMineur + \
                self.repartitionDoDMajeur + self.repartitionLaDMineur + self.repartitionFaMajeur + \
                self.repartitionReMineur + self.repartitionLaDMajeur + self.repartitionSolMineur + \
                self.repartitionReDMajeur + self.repartitionSolDMajeur + self.repartitionFaMineur
        from random import randrange
        nombreAleatoire = randrange(1, 7)
        if nombreAleatoire == 1:
            return "Do majeur"
        if nombreAleatoire == 2:
            return "Sol majeur"
        if nombreAleatoire == 3:
            return "Re majeur"
        if nombreAleatoire == 4:
            return "Fa majeur"
        if nombreAleatoire == 5:
            return "La# majeur"
        if nombreAleatoire == 6:
            return "Re# majeur"

    def repartitionMoyenne(self):
        return self.dissonnaceTotale / 360

    def dissonanceMoyenne(self):
        return self.repartitionTotale / 360
