import os
from random import randrange

import numpy as np
from EasyMIDI import EasyMIDI, Track, Note

from Gamme import Gamme
from Genre import Genre


class MarkovGen:

    # Constructeur
    def __init__(self, genre, markov1, markov2):
        ### Definition des notes
        self.c2 = Note('C', octave=3, duration=1 / 4, volume=100)  # DO2
        self.c2d = Note('C#', octave=3, duration=1 / 4, volume=100)
        self.d2 = Note('D', octave=3, duration=1 / 4, volume=100)
        self.d2d = Note('D#', octave=3, duration=1 / 4, volume=100)
        self.e2 = Note('E', octave=3, duration=1 / 4, volume=100)
        self.f2 = Note('F', octave=3, duration=1 / 4, volume=100)
        self.f2d = Note('F#', octave=3, duration=1 / 4, volume=100)
        self.g2 = Note('G', octave=3, duration=1 / 4, volume=100)
        self.g2d = Note('G#', octave=3, duration=1 / 4, volume=100)
        self.a2 = Note('A', octave=3, duration=1 / 4, volume=100)
        self.a2d = Note('A#', octave=3, duration=1 / 4, volume=100)
        self.b2 = Note('B', octave=3, duration=1 / 4, volume=100)
        self.c3 = Note('C', octave=4, duration=1 / 4, volume=100)  # DO3
        self.c3d = Note('C#', octave=4, duration=1 / 4, volume=100)
        self.d3 = Note('D', octave=4, duration=1 / 4, volume=100)
        self.d3d = Note('D#', octave=4, duration=1 / 4, volume=100)
        self.e3 = Note('E', octave=4, duration=1 / 4, volume=100)
        self.f3 = Note('F', octave=4, duration=1 / 4, volume=100)
        self.f3d = Note('F#', octave=4, duration=1 / 4, volume=100)
        self.g3 = Note('G', octave=4, duration=1 / 4, volume=100)
        self.g3d = Note('G#', octave=4, duration=1 / 4, volume=100)
        self.a3 = Note('A', octave=4, duration=1 / 4, volume=100)
        self.a3d = Note('A#', octave=4, duration=1 / 4, volume=100)
        self.b3 = Note('B', octave=4, duration=1 / 4, volume=100)
        self.c4 = Note('C', octave=5, duration=1 / 4, volume=100)  # DO4
        self.c4d = Note('C#', octave=5, duration=1 / 4, volume=100)
        self.d4 = Note('D', octave=5, duration=1 / 4, volume=100)
        self.d4d = Note('D#', octave=5, duration=1 / 4, volume=100)
        self.e4 = Note('E', octave=5, duration=1 / 4, volume=100)
        self.f4 = Note('F', octave=5, duration=1 / 4, volume=100)
        self.f4d = Note('F#', octave=5, duration=1 / 4, volume=100)
        self.g4 = Note('G', octave=5, duration=1 / 4, volume=100)
        self.g4d = Note('G#', octave=5, duration=1 / 4, volume=100)
        self.a4 = Note('A', octave=5, duration=1 / 4, volume=100)
        self.a4d = Note('A#', octave=5, duration=1 / 4, volume=100)
        self.b4 = Note('B', octave=5, duration=1 / 4, volume=100)
        ### Definition des gammes
        self.doma = Gamme('Do majeur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'])
        self.lami = Gamme('La mineur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'])
        self.solma = Gamme('Sol majeur', ['Do', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
        self.mimi = Gamme('Mi mineur', ['Do', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
        self.rema = Gamme('Re majeur', ['Dod', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
        self.simi = Gamme('Si mineur', ['Dod', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
        self.lama = Gamme('La majeur', ['Dod', 'Re', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
        self.fadmi = Gamme('Fad mineur', ['Dod', 'Re', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
        self.mima = Gamme('Mi majeur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
        self.dodmi = Gamme('Dod mineur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
        self.sima = Gamme('Si majeur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'Lad', 'Si'])
        self.soldmi = Gamme('Sold mineur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'Lad', 'Si'])
        self.fadma = Gamme('Fad majeur', ['Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad', 'Si'])
        self.redmi = Gamme('Red mineur', ['Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad', 'Si'])
        self.dodma = Gamme('Dod majeur', ['Do', 'Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad'])
        self.ladmi = Gamme('Lad mineur', ['Do', 'Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad'])
        self.fama = Gamme('Fa majeur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Lad'])
        self.remi = Gamme('Re mineur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Lad'])
        self.ladma = Gamme('Lad majeur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'La', 'Lad'])
        self.solmi = Gamme('Sol mineur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'La', 'Lad'])
        self.redma = Gamme('Red majeur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
        self.domi = Gamme('Do mineur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
        self.soldma = Gamme('Sold majeur', ['Do', 'Dod', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
        self.fami = Gamme('Fa mineur', ['Do', 'Dod', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
        self.markov = []  # tableau de markov
        self.markovtps = []  # tab de markov pour le temps
        for i in range(36):
            self.markov.append([0] * 36)
        self.markov = markov1[:]
        gamme = genre.chooseGenre()
        self.generate(gamme)

    # Generation avec Markov
    def generate(self, gamme):
        noteactuelle = ""
        notes = []
        if gamme == "Do majeur" or gamme == "La mineur":
            notes = self.doma.getNotes()
        if gamme == "Sol majeur" or gamme == "Mi mineur":
            notes = list(self.solma.getNotes())
        if gamme == "Re majeur" or gamme == "Si mineur":
            notes = list(self.redmi.getNotes())
        if gamme == "La majeur" or gamme == "Fa# mineur":
            notes = list(self.lama.getNotes())
        if gamme == "Mi majeur" or gamme == "Do# mineur":
            notes = list(self.mima.getNotes())
        if gamme == "Si majeur" or gamme == "Sol# mineur":
            notes = list(self.sima.getNotes())
        if gamme == "Fa# majeur" or gamme == "Re# mineur":
            notes = list(self.fadma.getNotes())
        if gamme == "Do# majeur" or gamme == "La# mineur":
            notes = list(self.dodma.getNotes())
        if gamme == "Fa majeur" or gamme == "Re mineur":
            notes = list(self.fama.getNotes())
        if gamme == "La# majeur" or gamme == "Sol mineur":
            notes = list(self.ladma.getNotes())
        if gamme == "Re# majeur" or gamme == "Do mineur":
            notes = list(self.redma.getNotes())
        if gamme == "Sol# majeur" or gamme == "Fa mineur":
            notes = list(self.soldma.getNotes())
        total = 0
        for i in range(36):
            for j in range(36):
                total += self.markov[i][j]
            for x in range(36):
                self.markov[i][x] = self.markov[i][x] / total
            total = 0
        for i in range(36):
            print(i, "|", self.markov[i])

        markovtps = ([[0.1, 0.3, 0.6, 0, 0],
                      [0.2, 0.2, 0.5, 0.1, 0],
                      [0.1, 0.1, 0.5, 0.2, 0.1],
                      [0, 0.05, 0.3, 0.6, 0.05],
                      [0, 0.05, 0.3, 0.35, 0.3]])
        print("Gamme du morceau généré : ", gamme)
        Genre.gamme = gamme
        easyMIDI = EasyMIDI()
        track1 = Track("acoustic grand piano")
        temps = [1, 1 / 2, 1 / 4, 1 / 8, 1 / 16]
        tempsrandom = randrange(0, 5)
        # Premiere note aléatoire dans la gamme
        notesrandom = randrange(0, 7)
        tempsactuelle = ""
        if notes[notesrandom] == "Do":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.c2.setDuration(temps[tempsrandom])
                track1.addNote(self.c2)
                noteactuelle = 0
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.c3.setDuration(temps[tempsrandom])
                track1.addNote(self.c3)
                noteactuelle = 12
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.c4.setDuration(temps[tempsrandom])
                track1.addNote(self.c4)
                noteactuelle = 24
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Dod":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.c2d.setDuration(temps[tempsrandom])
                track1.addNote(self.c2d)
                noteactuelle = 1
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.c3d.setDuration(temps[tempsrandom])
                track1.addNote(self.c3d)
                noteactuelle = 13
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.c4d.setDuration(temps[tempsrandom])
                track1.addNote(self.c4d)
                noteactuelle = 25
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Re":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.d2.setDuration(temps[tempsrandom])
                track1.addNote(self.d2)
                noteactuelle = 2
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.d3.setDuration(temps[tempsrandom])
                track1.addNote(self.d3)
                noteactuelle = 14
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.d4.setDuration(temps[tempsrandom])
                track1.addNote(self.d4)
                noteactuelle = 26
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Red":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.d2d.setDuration(temps[tempsrandom])
                track1.addNote(self.d2d)
                noteactuelle = 3
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.d3d.setDuration(temps[tempsrandom])
                track1.addNote(self.d3d)
                noteactuelle = 15
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.d4d.setDuration(temps[tempsrandom])
                track1.addNote(self.d4d)
                noteactuelle = 27
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Mi":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.e2.setDuration(temps[tempsrandom])
                track1.addNote(self.e2)
                noteactuelle = 4
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.e3.setDuration(temps[tempsrandom])
                track1.addNote(self.e3)
                noteactuelle = 16
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.e4.setDuration(temps[tempsrandom])
                track1.addNote(self.e4)
                noteactuelle = 28
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Fa":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.f2.setDuration(temps[tempsrandom])
                track1.addNote(self.f2)
                noteactuelle = 5
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.f3.setDuration(temps[tempsrandom])
                track1.addNote(self.f3)
                noteactuelle = 17
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.f4.setDuration(temps[tempsrandom])
                track1.addNote(self.f4)
                noteactuelle = 29
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Fad":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.f2d.setDuration(temps[tempsrandom])
                track1.addNote(self.f2d)
                noteactuelle = 6
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.f3d.setDuration(temps[tempsrandom])
                track1.addNote(self.f3d)
                noteactuelle = 18
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.f4d.setDuration(temps[tempsrandom])
                track1.addNote(self.f4d)
                noteactuelle = 30
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Sol":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.g2.setDuration(temps[tempsrandom])
                track1.addNote(self.g2)
                noteactuelle = 7
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.g3.setDuration(temps[tempsrandom])
                track1.addNote(self.g3)
                noteactuelle = 19
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.g4.setDuration(temps[tempsrandom])
                track1.addNote(self.g4)
                noteactuelle = 31
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Sold":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.g2d.setDuration(temps[tempsrandom])
                track1.addNote(self.g2d)
                noteactuelle = 8
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.g3d.setDuration(temps[tempsrandom])
                track1.addNote(self.g3d)
                noteactuelle = 20
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.g4d.setDuration(temps[tempsrandom])
                track1.addNote(self.g4d)
                noteactuelle = 32
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "La":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.a2.setDuration(temps[tempsrandom])
                track1.addNote(self.a2)
                noteactuelle = 9
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.a3.setDuration(temps[tempsrandom])
                track1.addNote(self.a3)
                noteactuelle = 21
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.a4.setDuration(temps[tempsrandom])
                track1.addNote(self.a4)
                noteactuelle = 33
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Lad":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.a2d.setDuration(temps[tempsrandom])
                track1.addNote(self.a2d)
                noteactuelle = 10
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.a3d.setDuration(temps[tempsrandom])
                track1.addNote(self.a3d)
                noteactuelle = 22
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.a4d.setDuration(temps[tempsrandom])
                track1.addNote(self.a4d)
                noteactuelle = 34
                tempsactuelle = tempsrandom
        if notes[notesrandom] == "Si":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                self.b2.setDuration(temps[tempsrandom])
                track1.addNote(self.b2)
                noteactuelle = 11
                tempsactuelle = tempsrandom
            if hauteur == 2:
                self.b3.setDuration(temps[tempsrandom])
                track1.addNote(self.b3)
                noteactuelle = 23
                tempsactuelle = tempsrandom
            if hauteur == 3:
                self.b4.setDuration(temps[tempsrandom])
                track1.addNote(self.b4)
                noteactuelle = 35
                tempsactuelle = tempsrandom

        taillemorceau = randrange(100, 200)
        counter = 0
        # on se base sur la premiere note pour generer les suivantes :
        while taillemorceau > counter:
            # selectionne la bonne ligne
            tab = np.array(self.markov[noteactuelle])
            tabtps = np.array(markovtps[tempsactuelle])

            # suit la loi de probabilité et selectionne une valeur
            notesuivantetab = np.random.choice(36, 1, p=tab)
            tempssuivanttab = np.random.choice(5, 1, p=tabtps)

            # récupération de la valeur
            notesuivante = int(notesuivantetab[0])
            tempssuivant = int(tempssuivanttab[0])

            if notesuivante == 0 and "Do" in notes:
                self.c2.setDuration(temps[tempssuivant])
                track1.addNote(self.c2)
                counter += 1
            if notesuivante == 1 and "Dod" in notes:
                self.c2d.setDuration(temps[tempssuivant])
                track1.addNote(self.c2d)
                counter += 1
            if notesuivante == 2 and "Re" in notes:
                self.d2.setDuration(temps[tempssuivant])
                track1.addNote(self.d2)
                counter += 1
            if notesuivante == 3 and "Red" in notes:
                self.d2d.setDuration(temps[tempssuivant])
                track1.addNote(self.d2d)
                counter += 1
            if notesuivante == 4 and "Mi" in notes:
                self.e2.setDuration(temps[tempssuivant])
                track1.addNote(self.e2)
                counter += 1
            if notesuivante == 5 and "Fa" in notes:
                self.f2.setDuration(temps[tempssuivant])
                track1.addNote(self.f2)
                counter += 1
            if notesuivante == 6 and "Fad" in notes:
                self.f2d.setDuration(temps[tempssuivant])
                track1.addNote(self.f2d)
                counter += 1
            if notesuivante == 7 and "Sol" in notes:
                self.g2.setDuration(temps[tempssuivant])
                track1.addNote(self.g2)
                counter += 1
            if notesuivante == 8 and "Sold" in notes:
                self.g2d.setDuration(temps[tempssuivant])
                track1.addNote(self.g2d)
                counter += 1
            if notesuivante == 9 and "La" in notes:
                self.a2.setDuration(temps[tempssuivant])
                track1.addNote(self.a2)
                counter += 1
            if notesuivante == 10 and "Lad" in notes:
                self.a2d.setDuration(temps[tempssuivant])
                track1.addNote(self.a2d)
                counter += 1
            if notesuivante == 11 and "Si" in notes:
                self.b2.setDuration(temps[tempssuivant])
                track1.addNote(self.b2)
                counter += 1
            if notesuivante == 12 and "Do" in notes:
                self.c3.setDuration(temps[tempssuivant])
                track1.addNote(self.c3)
                counter += 1
            if notesuivante == 13 and "Dod" in notes:
                self.c3d.setDuration(temps[tempssuivant])
                track1.addNote(self.c3d)
                counter += 1
            if notesuivante == 14 and "Re" in notes:
                self.d3.setDuration(temps[tempssuivant])
                track1.addNote(self.d3)
                counter += 1
            if notesuivante == 15 and "Red" in notes:
                self.d3d.setDuration(temps[tempssuivant])
                track1.addNote(self.d3d)
                counter += 1
            if notesuivante == 16 and "Mi" in notes:
                self.e3.setDuration(temps[tempssuivant])
                track1.addNote(self.e3)
                counter += 1
            if notesuivante == 17 and "Fa" in notes:
                self.f3.setDuration(temps[tempssuivant])
                track1.addNote(self.f3)
                counter += 1
            if notesuivante == 18 and "Fad" in notes:
                self.f3d.setDuration(temps[tempssuivant])
                track1.addNote(self.f3d)
                counter += 1
            if notesuivante == 19 and "Sol" in notes:
                self.g3.setDuration(temps[tempssuivant])
                track1.addNote(self.g3)
                counter += 1
            if notesuivante == 20 and "Sold" in notes:
                self.g3d.setDuration(temps[tempssuivant])
                track1.addNote(self.g3d)
                counter += 1
            if notesuivante == 21 and "La" in notes:
                self.a3.setDuration(temps[tempssuivant])
                track1.addNote(self.a3)
                counter += 1
            if notesuivante == 22 and "Lad" in notes:
                self.a3d.setDuration(temps[tempssuivant])
                track1.addNote(self.a3d)
                counter += 1
            if notesuivante == 23 and "Si" in notes:
                self.b3.setDuration(temps[tempssuivant])
                track1.addNote(self.b3)
                counter += 1
            if notesuivante == 24 and "Do" in notes:
                self.c4.setDuration(temps[tempssuivant])
                track1.addNote(self.c4)
                counter += 1
            if notesuivante == 25 and "Dod" in notes:
                self.c4d.setDuration(temps[tempssuivant])
                track1.addNote(self.c4d)
                counter += 1
            if notesuivante == 26 and "Re" in notes:
                self.d4.setDuration(temps[tempssuivant])
                track1.addNote(self.d4)
                counter += 1
            if notesuivante == 27 and "Red" in notes:
                self.d4d.setDuration(temps[tempssuivant])
                track1.addNote(self.d4d)
                counter += 1
            if notesuivante == 28 and "Mi" in notes:
                self.e4.setDuration(temps[tempssuivant])
                track1.addNote(self.e4)
                counter += 1
            if notesuivante == 29 and "Fa" in notes:
                self.f4.setDuration(temps[tempssuivant])
                track1.addNote(self.f4)
                counter += 1
            if notesuivante == 30 and "Fad" in notes:
                self.f4d.setDuration(temps[tempssuivant])
                track1.addNote(self.f4d)
                counter += 1
            if notesuivante == 31 and "Sol" in notes:
                self.g4.setDuration(temps[tempssuivant])
                track1.addNote(self.g4)
                counter += 1
            if notesuivante == 32 and "Sold" in notes:
                self.g4d.setDuration(temps[tempssuivant])
                track1.addNote(self.g4d)
                counter += 1
            if notesuivante == 33 and "La" in notes:
                self.a4.setDuration(temps[tempssuivant])
                track1.addNote(self.a4)
                counter += 1
            if notesuivante == 34 and "Lad" in notes:
                self.a4d.setDuration(temps[tempssuivant])
                track1.addNote(self.a4d)
                counter += 1
            if notesuivante == 35 and "Si" in notes:
                self.b4.setDuration(temps[tempssuivant])
                track1.addNote(self.b4)
                counter += 1
            noteactuelle = notesuivante
            tempsactuelle = tempssuivant

        try:
            os.remove("markov.mid")
        except:
            print("N'existe pas encore")
        easyMIDI.addTrack(track1)
        easyMIDI.writeMIDI("markov.mid")
        print("Song créé avec succès")
