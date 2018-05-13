from EasyMIDI import EasyMIDI, Track, Note
import numpy as np
from random import randrange
import os
from Gamme import Gamme
class MarkovGen:
    ### Definition des notes
    c2 = Note('C', octave=3, duration=1 / 4, volume=100)  # DO2
    c2d = Note('C#', octave=3, duration=1 / 4, volume=100)
    d2 = Note('D', octave=3, duration=1 / 4, volume=100)
    d2d = Note('D#', octave=3, duration=1 / 4, volume=100)
    e2 = Note('E', octave=3, duration=1 / 4, volume=100)
    f2 = Note('F', octave=3, duration=1 / 4, volume=100)
    f2d = Note('F#', octave=3, duration=1 / 4, volume=100)
    g2 = Note('G', octave=3, duration=1 / 4, volume=100)
    g2d = Note('G#', octave=3, duration=1 / 4, volume=100)
    a2 = Note('A', octave=3, duration=1 / 4, volume=100)
    a2d = Note('A#', octave=3, duration=1 / 4, volume=100)
    b2 = Note('B', octave=3, duration=1 / 4, volume=100)
    c3 = Note('C', octave=4, duration=1 / 4, volume=100)  # DO3
    c3d = Note('C#', octave=4, duration=1 / 4, volume=100)
    d3 = Note('D', octave=4, duration=1 / 4, volume=100)
    d3d = Note('D#', octave=4, duration=1 / 4, volume=100)
    e3 = Note('E', octave=4, duration=1 / 4, volume=100)
    f3 = Note('F', octave=4, duration=1 / 4, volume=100)
    f3d = Note('F#', octave=4, duration=1 / 4, volume=100)
    g3 = Note('G', octave=4, duration=1 / 4, volume=100)
    g3d = Note('G#', octave=4, duration=1 / 4, volume=100)
    a3 = Note('A', octave=4, duration=1 / 4, volume=100)
    a3d = Note('A#', octave=4, duration=1 / 4, volume=100)
    b3 = Note('B', octave=4, duration=1 / 4, volume=100)
    c4 = Note('C', octave=5, duration=1 / 4, volume=100)  # DO4
    c4d = Note('C#', octave=5, duration=1 / 4, volume=100)
    d4 = Note('D', octave=5, duration=1 / 4, volume=100)
    d4d = Note('D#', octave=5, duration=1 / 4, volume=100)
    e4 = Note('E', octave=5, duration=1 / 4, volume=100)
    f4 = Note('F', octave=5, duration=1 / 4, volume=100)
    f4d = Note('F#', octave=5, duration=1 / 4, volume=100)
    g4 = Note('G', octave=5, duration=1 / 4, volume=100)
    g4d = Note('G#', octave=5, duration=1 / 4, volume=100)
    a4 = Note('A', octave=5, duration=1 / 4, volume=100)
    a4d = Note('A#', octave=5, duration=1 / 4, volume=100)
    b4 = Note('B', octave=5, duration=1 / 4, volume=100)
    ### Definition des gammes
    doma = Gamme('Do majeur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'])
    lami = Gamme('La mineur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'])
    solma = Gamme('Sol majeur', ['Do', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
    mimi = Gamme('Mi mineur', ['Do', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
    rema = Gamme('Re majeur', ['Dod', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
    simi = Gamme('Si mineur', ['Dod', 'Re', 'Mi', 'Fad', 'Sol', 'La', 'Si'])
    lama = Gamme('La majeur', ['Dod', 'Re', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
    fadmi = Gamme('Fad mineur', ['Dod', 'Re', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
    mima = Gamme('Mi majeur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
    dodmi = Gamme('Dod mineur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'La', 'Si'])
    sima = Gamme('Si majeur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'Lad', 'Si'])
    soldmi = Gamme('Sold mineur', ['Dod', 'Red', 'Mi', 'Fad', 'Sold', 'Lad', 'Si'])
    fadma = Gamme('Fad majeur', ['Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad', 'Si'])
    redmi = Gamme('Red mineur', ['Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad', 'Si'])
    dodma = Gamme('Dod majeur', ['Do', 'Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad'])
    ladmi = Gamme('Lad mineur', ['Do', 'Dod', 'Red', 'Fa', 'Fad', 'Sold', 'Lad'])
    fama = Gamme('Fa majeur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Lad'])
    remi = Gamme('Re mineur', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Lad'])
    ladma = Gamme('Lad majeur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'La', 'Lad'])
    solmi = Gamme('Sol mineur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'La', 'Lad'])
    redma = Gamme('Red majeur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
    domi = Gamme('Do mineur', ['Do', 'Re', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
    soldma = Gamme('Sold majeur', ['Do', 'Dod', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
    fami = Gamme('Fa mineur', ['Do', 'Dod', 'Red', 'Fa', 'Sol', 'Sold', 'Lad'])
    markov = []  # tableau de markov

    def __init__(self, genre, markov1):
        for i in range(36):
            self.markov.append([0] * 36)
        self.markov = markov1[:]
        gamme = genre.chooseGenre()
        self.generate(gamme)

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
                self.markov[i][x] = self.markov[i][x]/total
            total = 0
        for i in range(36):
            print(i, "|", self.markov[i])

        easyMIDI = EasyMIDI()
        track1 = Track("acoustic grand piano")
        notesrandom = randrange(0, 7)
        if notes[notesrandom] == "Do":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.c2)
                noteactuelle = 0
            if hauteur == 2:
                track1.addNote(self.c3)
                noteactuelle = 12
            if hauteur == 3:
                track1.addNote(self.c4)
                noteactuelle = 24
        if notes[notesrandom] == "Dod":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.c2d)
                noteactuelle = 1
            if hauteur == 2:
                track1.addNote(self.c3d)
                noteactuelle = 13
            if hauteur == 3:
                track1.addNote(self.c4d)
                noteactuelle = 25
        if notes[notesrandom] == "Re":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.d2)
                noteactuelle = 2
            if hauteur == 2:
                track1.addNote(self.d3)
                noteactuelle = 14
            if hauteur == 3:
                track1.addNote(self.d4)
                noteactuelle = 26
        if notes[notesrandom] == "Red":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.d2d)
                noteactuelle = 3
            if hauteur == 2:
                track1.addNote(self.d3d)
                noteactuelle = 15
            if hauteur == 3:
                track1.addNote(self.d4d)
                noteactuelle = 27
        if notes[notesrandom] == "Mi":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.e2)
                noteactuelle = 4
            if hauteur == 2:
                track1.addNote(self.e3)
                noteactuelle = 16
            if hauteur == 3:
                track1.addNote(self.e4)
                noteactuelle = 28
        if notes[notesrandom] == "Fa":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.f2)
                noteactuelle = 5
            if hauteur == 2:
                track1.addNote(self.f3)
                noteactuelle = 17
            if hauteur == 3:
                track1.addNote(self.f4)
                noteactuelle = 29
        if notes[notesrandom] == "Fad":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.f2d)
                noteactuelle = 6
            if hauteur == 2:
                track1.addNote(self.f3d)
                noteactuelle = 18
            if hauteur == 3:
                track1.addNote(self.f4d)
                noteactuelle = 30
        if notes[notesrandom] == "Sol":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.g2)
                noteactuelle = 7
            if hauteur == 2:
                track1.addNote(self.g3)
                noteactuelle = 19
            if hauteur == 3:
                track1.addNote(self.g4)
                noteactuelle = 31
        if notes[notesrandom] == "Sold":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.g2d)
                noteactuelle = 8
            if hauteur == 2:
                track1.addNote(self.g3d)
                noteactuelle = 20
            if hauteur == 3:
                track1.addNote(self.g4d)
                noteactuelle = 32
        if notes[notesrandom] == "La":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.a2)
                noteactuelle = 9
            if hauteur == 2:
                track1.addNote(self.a3)
                noteactuelle = 21
            if hauteur == 3:
                track1.addNote(self.a4)
                noteactuelle = 33
        if notes[notesrandom] == "Lad":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.a2d)
                noteactuelle = 10
            if hauteur == 2:
                track1.addNote(self.a3d)
                noteactuelle = 22
            if hauteur == 3:
                track1.addNote(self.a4d)
                noteactuelle = 34
        if notes[notesrandom] == "Si":
            hauteur = randrange(1, 4)
            if hauteur == 1:
                track1.addNote(self.b2)
                noteactuelle = 11
            if hauteur == 2:
                track1.addNote(self.b3)
                noteactuelle = 23
            if hauteur == 3:
                track1.addNote(self.b4)
                noteactuelle = 35

        taillemorceau = randrange(100, 200)
        counter = 0
        # on se base sur la premiere note pour generer les suivantes :
        while taillemorceau > counter:
            tab = np.array(self.markov[noteactuelle])
            notesuivantetab = np.random.choice(36, 1, p = tab)
            notesuivante = int(notesuivantetab[0])
            if notesuivante == 0 and "Do" in notes:
                track1.addNote(self.c2)
                counter += 1
            if notesuivante == 1 and "Dod" in notes:
                track1.addNote(self.c2d)
                counter += 1
            if notesuivante == 2 and "Re" in notes:
                track1.addNote(self.d2)
                counter += 1
            if notesuivante == 3 and "Red" in notes:
                track1.addNote(self.d2d)
                counter += 1
            if notesuivante == 4 and "Mi" in notes:
                track1.addNote(self.e2)
                counter += 1
            if notesuivante == 5 and "Fa" in notes:
                track1.addNote(self.f2)
                counter += 1
            if notesuivante == 6 and "Fad" in notes:
                track1.addNote(self.f2d)
                counter += 1
            if notesuivante == 7 and "Sol" in notes:
                track1.addNote(self.g2)
                counter += 1
            if notesuivante == 8 and "Sold" in notes:
                track1.addNote(self.g2d)
                counter += 1
            if notesuivante == 9 and "La" in notes:
                track1.addNote(self.a2)
                counter += 1
            if notesuivante == 10 and "Lad" in notes:
                track1.addNote(self.a2d)
                counter += 1
            if notesuivante == 11 and "Si" in notes:
                track1.addNote(self.b2)
                counter += 1
            if notesuivante == 12 and "Do" in notes:
                track1.addNote(self.c3)
                counter += 1
            if notesuivante == 13 and "Dod" in notes:
                track1.addNote(self.c3d)
                counter += 1
            if notesuivante == 14 and "Re" in notes:
                track1.addNote(self.d3)
                counter += 1
            if notesuivante == 15 and "Red" in notes:
                track1.addNote(self.d3d)
                counter += 1
            if notesuivante == 16 and "Mi" in notes:
                track1.addNote(self.e3)
                counter += 1
            if notesuivante == 17 and "Fa" in notes:
                track1.addNote(self.f3)
                counter += 1
            if notesuivante == 18 and "Fad" in notes:
                track1.addNote(self.f3d)
                counter += 1
            if notesuivante == 19 and "Sol" in notes:
                track1.addNote(self.g3)
                counter += 1
            if notesuivante == 20 and "Sold" in notes:
                track1.addNote(self.g3d)
                counter += 1
            if notesuivante == 21 and "La" in notes:
                track1.addNote(self.a3)
                counter += 1
            if notesuivante == 22 and "Lad" in notes:
                track1.addNote(self.a3d)
                counter += 1
            if notesuivante == 23 and "Si" in notes:
                track1.addNote(self.b3)
                counter += 1
            if notesuivante == 24 and "Do" in notes:
                track1.addNote(self.c4)
                counter += 1
            if notesuivante == 25 and "Dod" in notes:
                track1.addNote(self.c4d)
                counter += 1
            if notesuivante == 26 and "Re" in notes:
                track1.addNote(self.d4)
                counter += 1
            if notesuivante == 27 and "Red" in notes:
                track1.addNote(self.d4d)
                counter += 1
            if notesuivante == 28 and "Mi" in notes:
                track1.addNote(self.e4)
                counter += 1
            if notesuivante == 29 and "Fa" in notes:
                track1.addNote(self.f4)
                counter += 1
            if notesuivante == 30 and "Fad" in notes:
                track1.addNote(self.f4d)
                counter += 1
            if notesuivante == 31 and "Sol" in notes:
                track1.addNote(self.g4)
                counter += 1
            if notesuivante == 32 and "Sold" in notes:
                track1.addNote(self.g4d)
                counter += 1
            if notesuivante == 33 and "La" in notes:
                track1.addNote(self.a4)
                counter += 1
            if notesuivante == 34 and "Lad" in notes:
                track1.addNote(self.a4d)
                counter += 1
            if notesuivante == 35 and "Si" in notes:
                track1.addNote(self.b4)
                counter += 1
            noteactuelle = notesuivante

        try:
            os.remove("markov.mid")
        except:
            print("N'existe pas encore")
        easyMIDI.addTrack(track1)
        easyMIDI.writeMIDI("markov.mid")
        print("Song créé avec succès")
        # npr.choice([a1, ..., an], p=[p1, ..., pn], size=n): tirages
        # indép.dans[a1, ..., an]
        # de
        # loi[p1, ..., pn]


