import os
from random import randrange

from EasyMIDI import EasyMIDI, Track, Note

from Gamme import Gamme


class AleatoireGen:

    # Constructeur
    def __init__(self, genre):
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

        self.dissonnance = 0
        gamme = genre.chooseGenre()
        print(gamme)
        dissonnance = genre.dissonanceMoyenne() - 10
        self.generate(gamme, dissonnance)

    # Generation musique
    def generate(self, gamme, dissonnance):
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

        counter = 0
        # definition longueur morceau (100 à 200 notes)
        taillemorceau = randrange(100, 200)
        dissonnanceactuelle = 100

        easyMIDI = EasyMIDI()
        track1 = Track("acoustic grand piano")  # oops

        while counter < taillemorceau:
            # On ajoute une note de la gamme
            notesrandom = randrange(0, 7)
            tempsrandom = randrange(0, 5)
            temps = [1, 1 / 2, 1 / 4, 1 / 8, 1 / 16]
            if notes[notesrandom] == "Do":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.c2.setDuration(temps[tempsrandom])
                    track1.addNote(self.c2)
                if hauteur == 2:
                    self.c3.setDuration(temps[tempsrandom])
                    track1.addNote(self.c3)
                if hauteur == 3:
                    self.c4.setDuration(temps[tempsrandom])
                    track1.addNote(self.c4)
            if notes[notesrandom] == "Dod":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.c2d.setDuration(temps[tempsrandom])
                    track1.addNote(self.c2d)
                if hauteur == 2:
                    self.c3d.setDuration(temps[tempsrandom])
                    track1.addNote(self.c3d)
                if hauteur == 3:
                    self.c4d.setDuration(temps[tempsrandom])
                    track1.addNote(self.c4d)
            if notes[notesrandom] == "Re":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.d2.setDuration(temps[tempsrandom])
                    track1.addNote(self.d2)
                if hauteur == 2:
                    self.d3.setDuration(temps[tempsrandom])
                    track1.addNote(self.d3)
                if hauteur == 3:
                    self.d4.setDuration(temps[tempsrandom])
                    track1.addNote(self.d4)
            if notes[notesrandom] == "Red":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.d2d.setDuration(temps[tempsrandom])
                    track1.addNote(self.d2d)
                if hauteur == 2:
                    self.d3d.setDuration(temps[tempsrandom])
                    track1.addNote(self.d3d)
                if hauteur == 3:
                    self.d4d.setDuration(temps[tempsrandom])
                    track1.addNote(self.d4d)
            if notes[notesrandom] == "Mi":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.e2.setDuration(temps[tempsrandom])
                    track1.addNote(self.e2)
                if hauteur == 2:
                    self.e3.setDuration(temps[tempsrandom])
                    track1.addNote(self.e3)
                if hauteur == 3:
                    self.e4.setDuration(temps[tempsrandom])
                    track1.addNote(self.e4)
            if notes[notesrandom] == "Fa":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.f2.setDuration(temps[tempsrandom])
                    track1.addNote(self.f2)
                if hauteur == 2:
                    self.f3.setDuration(temps[tempsrandom])
                    track1.addNote(self.f3)
                if hauteur == 3:
                    self.f4.setDuration(temps[tempsrandom])
                    track1.addNote(self.f4)
            if notes[notesrandom] == "Fad":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.f2d.setDuration(temps[tempsrandom])
                    track1.addNote(self.f2d)
                if hauteur == 2:
                    self.f3d.setDuration(temps[tempsrandom])
                    track1.addNote(self.f3d)
                if hauteur == 3:
                    self.f4d.setDuration(temps[tempsrandom])
                    track1.addNote(self.f4d)
            if notes[notesrandom] == "Sol":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.g2.setDuration(temps[tempsrandom])
                    track1.addNote(self.g2)
                if hauteur == 2:
                    self.g3.setDuration(temps[tempsrandom])
                    track1.addNote(self.g3)
                if hauteur == 3:
                    self.g4.setDuration(temps[tempsrandom])
                    track1.addNote(self.g4)
            if notes[notesrandom] == "Sold":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.g2d.setDuration(temps[tempsrandom])
                    track1.addNote(self.g2d)
                if hauteur == 2:
                    self.g3d.setDuration(temps[tempsrandom])
                    track1.addNote(self.g3d)
                if hauteur == 3:
                    self.g4d.setDuration(temps[tempsrandom])
                    track1.addNote(self.g4d)
            if notes[notesrandom] == "La":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.a2.setDuration(temps[tempsrandom])
                    track1.addNote(self.a2)
                if hauteur == 2:
                    self.a3.setDuration(temps[tempsrandom])
                    track1.addNote(self.a3)
                if hauteur == 3:
                    self.a4.setDuration(temps[tempsrandom])
                    track1.addNote(self.a4)
            if notes[notesrandom] == "Lad":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.a2d.setDuration(temps[tempsrandom])
                    track1.addNote(self.a2d)
                if hauteur == 2:
                    self.a3d.setDuration(temps[tempsrandom])
                    track1.addNote(self.a3d)
                if hauteur == 3:
                    self.a4d.setDuration(temps[tempsrandom])
                    track1.addNote(self.a4d)
            if notes[notesrandom] == "Si":
                hauteur = randrange(1, 4)
                if hauteur == 1:
                    self.b2.setDuration(temps[tempsrandom])
                    track1.addNote(self.b2)
                if hauteur == 2:
                    self.b3.setDuration(temps[tempsrandom])
                    track1.addNote(self.b3)
                if hauteur == 3:
                    self.b4.setDuration(temps[tempsrandom])
                    track1.addNote(self.b4)

            counter = counter + 1
        print("Dissonnance du morceau créé : ", dissonnanceactuelle / 8)
        try:
            os.remove("random.mid")
        except:
            print("N'existe pas encore")
        easyMIDI.addTrack(track1)
        easyMIDI.writeMIDI("random.mid")
        print("Song créé avec succès")
