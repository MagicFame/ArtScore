from Gamme import Gamme
from mido import Message, MidiFile, MidiTrack
from EasyMIDI import EasyMIDI, Track, Note, Chord, RomanChord


class AleatoireGen:
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

    dissonnance = 0

    def __init__(self, genre):
        gamme = genre.chooseGenre()
        print(gamme)
        dissonnance = genre.dissonanceMoyenne() - 10
        self.generate(gamme, dissonnance)

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

        from random import randrange
        counter = 0
        # definition longueur morceau (100 à 200 notes)
        taillemorceau = randrange(100, 200)
        dissonnanceactuelle = 100

        easyMIDI = EasyMIDI()
        track1 = Track("acoustic grand piano")  # oops

        while counter < taillemorceau:
            if dissonnanceactuelle >= dissonnance:  # On ajoute une note de la gamme
                notesrandom = randrange(0, 7)
                if notes[notesrandom] == "Do":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.c2)
                    if hauteur == 2:
                        track1.addNote(self.c3)
                    if hauteur == 3:
                        track1.addNote(self.c4)
                if notes[notesrandom] == "Dod":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.c2d)
                    if hauteur == 2:
                        track1.addNote(self.c3d)
                    if hauteur == 3:
                        track1.addNote(self.c4d)
                if notes[notesrandom] == "Re":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.d2)
                    if hauteur == 2:
                        track1.addNote(self.d3)
                    if hauteur == 3:
                        track1.addNote(self.d4)
                if notes[notesrandom] == "Red":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.d2d)
                    if hauteur == 2:
                        track1.addNote(self.d3d)
                    if hauteur == 3:
                        track1.addNote(self.d4d)
                if notes[notesrandom] == "Mi":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.e2)
                    if hauteur == 2:
                        track1.addNote(self.e3)
                    if hauteur == 3:
                        track1.addNote(self.e4)
                if notes[notesrandom] == "Fa":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.f2)
                    if hauteur == 2:
                        track1.addNote(self.f3)
                    if hauteur == 3:
                        track1.addNote(self.f4)
                if notes[notesrandom] == "Fad":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.f2d)
                    if hauteur == 2:
                        track1.addNote(self.f3d)
                    if hauteur == 3:
                        track1.addNote(self.f4d)
                if notes[notesrandom] == "Sol":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.g2)
                    if hauteur == 2:
                        track1.addNote(self.g3)
                    if hauteur == 3:
                        track1.addNote(self.g4)
                if notes[notesrandom] == "Sold":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.g2d)
                    if hauteur == 2:
                        track1.addNote(self.g3d)
                    if hauteur == 3:
                        track1.addNote(self.g4d)
                if notes[notesrandom] == "La":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.a2)
                    if hauteur == 2:
                        track1.addNote(self.a3)
                    if hauteur == 3:
                        track1.addNote(self.a4)
                if notes[notesrandom] == "Lad":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.a2d)
                    if hauteur == 2:
                        track1.addNote(self.a3d)
                    if hauteur == 3:
                        track1.addNote(self.a4d)
                if notes[notesrandom] == "Si":
                    hauteur = randrange(1, 4)
                    if hauteur == 1:
                        track1.addNote(self.b2)
                    if hauteur == 2:
                        track1.addNote(self.b3)
                    if hauteur == 3:
                        track1.addNote(self.b4)
            else:  # on ajoute une note random
                notesrandom = randrange(1, 13)
                hauteur = randrange(1, 4)
                if notesrandom == 1:
                    if hauteur == 1:
                        track1.addNote(self.c2)
                    if hauteur == 2:
                        track1.addNote(self.c3)
                    if hauteur == 3:
                        track1.addNote(self.c4)
                if notesrandom == 2:
                    if hauteur == 1:
                        track1.addNote(self.c2d)
                    if hauteur == 2:
                        track1.addNote(self.c3d)
                    if hauteur == 3:
                        track1.addNote(self.c4d)
                if notesrandom == 3:
                    if hauteur == 1:
                        track1.addNote(self.d2)
                    if hauteur == 2:
                        track1.addNote(self.d3)
                    if hauteur == 3:
                        track1.addNote(self.d4)
                if notesrandom == 4:
                    if hauteur == 1:
                        track1.addNote(self.d2d)
                    if hauteur == 2:
                        track1.addNote(self.d3d)
                    if hauteur == 3:
                        track1.addNote(self.d4d)
                if notesrandom == 5:
                    if hauteur == 1:
                        track1.addNote(self.e2)
                    if hauteur == 2:
                        track1.addNote(self.e3)
                    if hauteur == 3:
                        track1.addNote(self.e4)
                if notesrandom == 6:
                    if hauteur == 1:
                        track1.addNote(self.f2)
                    if hauteur == 2:
                        track1.addNote(self.f3)
                    if hauteur == 3:
                        track1.addNote(self.f4)
                if notesrandom == 7:
                    if hauteur == 1:
                        track1.addNote(self.f2d)
                    if hauteur == 2:
                        track1.addNote(self.f3d)
                    if hauteur == 3:
                        track1.addNote(self.f4d)
                if notesrandom == 8:
                    if hauteur == 1:
                        track1.addNote(self.g2)
                    if hauteur == 2:
                        track1.addNote(self.g3)
                    if hauteur == 3:
                        track1.addNote(self.g4)
                if notesrandom == 9:
                    if hauteur == 1:
                        track1.addNote(self.g2d)
                    if hauteur == 2:
                        track1.addNote(self.g3d)
                    if hauteur == 3:
                        track1.addNote(self.g4d)
                if notesrandom == 10:
                    if hauteur == 1:
                        track1.addNote(self.a2)
                    if hauteur == 2:
                        track1.addNote(self.a3)
                    if hauteur == 3:
                        track1.addNote(self.a4)
                if notesrandom == 11:
                    if hauteur == 1:
                        track1.addNote(self.a2d)
                    if hauteur == 2:
                        track1.addNote(self.a3d)
                    if hauteur == 3:
                        track1.addNote(self.a4d)
                if notesrandom == 12:
                    if hauteur == 1:
                        track1.addNote(self.b2)
                    if hauteur == 2:
                        track1.addNote(self.b3)
                    if hauteur == 3:
                        track1.addNote(self.b4)
            counter = counter + 1
            #print(counter)
        print("Dissonnance du morceau créé : ", dissonnanceactuelle)

        easyMIDI.addTrack(track1)
        easyMIDI.writeMIDI("output.mid")
        print("Song créé avec succès")
