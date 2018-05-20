from random import randrange


class Genre:

    # constructeur
    def __init__(self, nom):
        self.repartitionDoMajeur = 0
        self.repartitionDoMineur = 0
        self.repartitionLaMineur = 0
        self.repartitionSolMajeur = 0
        self.repartitionMiMineur = 0
        self.repartitionReMajeur = 0
        self.repartitionSiMineur = 0
        self.repartitionLaMajeur = 0
        self.repartitionFaDMineur = 0
        self.repartitionMiMajeur = 0
        self.repartitionDoDMineur = 0
        self.repartitionSiMajeur = 0
        self.repartitionSolDMineur = 0
        self.repartitionFaDMajeur = 0
        self.repartitionReDMineur = 0
        self.repartitionDoDMajeur = 0
        self.repartitionLaDMineur = 0
        self.repartitionFaMajeur = 0
        self.repartitionReMineur = 0
        self.repartitionLaDMajeur = 0
        self.repartitionSolMineur = 0
        self.repartitionReDMajeur = 0
        self.repartitionSolDMajeur = 0
        self.repartitionFaMineur = 0

        self.dissonnanceTotale = 0
        self.repartitionTotale = 0
        self.nom = nom
        self.notes = []
        self.gam = ""

    # Calcul du nombre d'occurence d'une gamme pour un genre donné
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

    # Calcul de la dissonnance totale pour un genre donné
    def addDissonance(self, value):
        self.dissonnanceTotale += value

    # Calcul de la répartition pour un genre (Note la plus élevée - la plus basse)
    def addRepartition(self, value):
        self.repartitionTotale += value

    # Affichage des caracteristiques propres à un genre
    def afficherInfoGenre(self):
        print("\n \n \n***************************** \nStyle selectionné : Classique")
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
        print("\nDissonnance moyenne :", self.dissonnanceTotale / 360)
        print("\nRepartition moyenne", self.repartitionTotale / 360, "\n\n***************************** \n\n")

    # Selectionne un genre en fonction des pourcentages
    def chooseGenre(self):
        gamme = []
        repartition = [self.repartitionDoMajeur, self.repartitionDoMineur, self.repartitionLaMineur,
                       self.repartitionSolMajeur, self.repartitionMiMineur, self.repartitionReMajeur,
                       self.repartitionSiMineur, self.repartitionLaMajeur, self.repartitionFaDMineur,
                       self.repartitionMiMajeur, self.repartitionDoDMineur, self.repartitionSiMajeur,
                       self.repartitionSolDMineur, self.repartitionFaDMajeur, self.repartitionReDMineur,
                       self.repartitionDoDMajeur, self.repartitionLaDMineur, self.repartitionFaMajeur,
                       self.repartitionReMineur, self.repartitionLaDMajeur, self.repartitionSolMineur,
                       self.repartitionReDMajeur, self.repartitionSolDMajeur, self.repartitionFaMineur]
        nomgamme = ["Do majeur", "Do mineur", "La mineur", "Sol majeur", "Mi mineur", "Re majeur", "Si mineur",
                    "La majeur", "Fa# mineur", "Mi majeur", "Do# mineur", "Si majeur", "Sol# mineur", "Fa# majeur",
                    "Re# mineur", "Do# majeur", "La# mineur", "Fa majeur", "Re mineur", "La# majeur", "Sol mineur",
                    "Re# majeur", "Sol# majeur", "Fa mineur"]
        for i in range(0, 6):
            value = repartition.index(max(repartition))
            gamme.append(nomgamme[value])
            del repartition[value]
            del nomgamme[value]
        print(gamme)
        nombreAleatoire = randrange(1, 7)
        if nombreAleatoire == 1:
            return gamme[0]
        if nombreAleatoire == 2:
            return gamme[1]
        if nombreAleatoire == 3:
            return gamme[2]
        if nombreAleatoire == 4:
            return gamme[3]
        if nombreAleatoire == 5:
            return gamme[4]
        if nombreAleatoire == 6:
            return gamme[5]

    # Calcul de la répartition moyenne
    def repartitionMoyenne(self):
        return self.dissonnanceTotale / 360

    # Calcul de la dissonnace moyenne
    def dissonanceMoyenne(self):
        return self.repartitionTotale / 360
