from EasyMIDI import EasyMIDI, Track, Note, Chord, RomanChord
from random import choice
import mido
from mido import MidiFile
import Gamme
from math import *


def trier(liste):  # Algorithme de tri afin d'avoir les notes de la gamme trié par ordre de Do à Si
    gamme = []
    if "Do" in liste:
        gamme.append("Do")
    if "Do#" in liste:
        gamme.append("Do#")
    if "Re" in liste:
        gamme.append("Re")
    if "Re#" in liste:
        gamme.append("Re#")
    if "Mi" in liste:
        gamme.append("Mi")
    if "Fa" in liste:
        gamme.append("Fa")
    if "Fa#" in liste:
        gamme.append("Fa#")
    if "Sol" in liste:
        gamme.append("Sol")
    if "Sol#" in liste:
        gamme.append("Sol#")
    if "La" in liste:
        gamme.append("La")
    if "La#" in liste:
        gamme.append("La#")
    if "Si" in liste:
        gamme.append("Si")

    return gamme


def detectRepartition():  # Detecte la différence entre la plus haute note et la plus basse note
    basse = int(notes[0])
    haute = int(notes[0])
    for n in notes:
        if int(n) > haute:
            haute = int(n)
        elif int(n) < basse:
            basse = int(n)
    print("Note haute :", haute, " et note basse : ", basse)
    return haute - basse


def detectGamme():  # Algorithme de détection de gamme basé sur les probabilitées.
    gamme = []
    comptdo = 0
    comptdod = 0
    comptre = 0
    comptred = 0
    comptmi = 0
    comptfa = 0
    comptfad = 0
    comptsol = 0
    comptsold = 0
    comptla = 0
    comptlad = 0
    comptsi = 0
    for n in notes:

        if int(n) % 12 == 0:
            comptdo += 1
        elif int(n) % 12 == 1:
            comptdod += 1
        elif int(n) % 12 == 2:
            comptre += 1
        elif int(n) % 12 == 3:
            comptred += 1
        elif int(n) % 12 == 4:
            comptmi += 1
        elif int(n) % 12 == 5:
            comptfa += 1
        elif int(n) % 12 == 6:
            comptfad += 1
        elif int(n) % 12 == 7:
            comptsol += 1
        elif int(n) % 12 == 8:
            comptsold += 1
        elif int(n) % 12 == 9:
            comptla += 1
        elif int(n) % 12 == 10:
            comptlad += 1
        elif int(n) % 12 == 11:
            comptsi += 1
    initial = (int(notes[0]) % 12)
    print("DO : ", comptdo, " DO# :", comptdod, " RE :", comptre, " RE# :", comptred, " MI :", comptmi, " FA :",
          comptfa, " FA# :", comptfad, " SOL :", comptsol, " SOL# :", comptsold, " LA :", comptla, " LA# :", comptlad,
          " SI :", comptsi)
    notesTotales = comptdo + comptdod + comptre + comptred + comptmi + comptfa + comptfad + comptsol + comptsold + \
                   comptla + comptlad + comptsi
    freqDo = round((comptdo / notesTotales) * 100)
    freqDod = round((comptdod / notesTotales) * 100)
    freqRe = round((comptre / notesTotales) * 100)
    freqRed = round((comptred / notesTotales) * 100)
    freqMi = round((comptmi / notesTotales) * 100)
    freqFa = round((comptfa / notesTotales) * 100)
    freqFad = round((comptfad / notesTotales) * 100)
    freqSol = round((comptsol / notesTotales) * 100)
    freqSold = round((comptsold / notesTotales) * 100)
    freqLa = round((comptla / notesTotales) * 100)
    freqLad = round((comptlad / notesTotales) * 100)
    freqSi = round((comptsi / notesTotales) * 100)
    print("DO : ", freqDo, "% DO# :", freqDod, "% RE :", freqRe, "% RE# :", freqRed, "% MI :", freqMi, "% FA :",
          freqFa, "% FA# :", freqFad, "% SOL :", freqSol, "% SOL# :", freqSold, "% LA :", freqLa, "% LA# :", freqLad,
          "% SI :", freqSi)
    if freqDo >= 10:
        gamme.append("Do")
    if freqDod >= 10:
        gamme.append("Do#")
    if freqRe >= 10:
        gamme.append("Re")
    if freqRed >= 10:
        gamme.append("Re#")
    if freqMi >= 10:
        gamme.append("Mi")
    if freqFa >= 10:
        gamme.append("Fa")
    if freqFad >= 10:
        gamme.append("Fa#")
    if freqSol >= 10:
        gamme.append("Sol")
    if freqSold >= 10:
        gamme.append("Sol#")
    if freqLa >= 10:
        gamme.append("La")
    if freqLad >= 10:
        gamme.append("La#")
    if freqSi >= 10:
        gamme.append("Si")
    print(gamme)
    if "Do" not in gamme and "Do#" not in gamme:
        if freqDo >= freqDod:
            gamme.insert(0, "Do")
        else:
            gamme.insert(0, "Do#")
    if "Do#" not in gamme and "Re" not in gamme:
        if freqDod >= freqRe:
            gamme.insert(0, "Do#")
        else:
            gamme.insert(1, "Re")
    if "Re" not in gamme and "Re#" not in gamme:
        if freqRe >= freqRed:
            gamme.insert(1, "Re")
        else:
            gamme.insert(1, "Re#")
    if "Re#" not in gamme and "Mi" not in gamme:
        if freqRed >= freqMi:
            gamme.insert(2, "Re#")
        else:
            gamme.insert(2, "Mi")
    if "Mi" not in gamme and "Fa" not in gamme:
        if freqMi >= freqFa:
            gamme.insert(2, "Mi")
        else:
            gamme.insert(3, "Fa")
    if "Fa" not in gamme and "Fa#" not in gamme:
        if freqFa >= freqFad:
            gamme.insert(3, "Fa")
        else:
            gamme.insert(3, "Fa#")
    if "Fa#" not in gamme and "Sol" not in gamme:
        if freqFad >= freqSol:
            gamme.insert(4, "Fa#")
        else:
            gamme.insert(4, "Sol")
    if "Sol" not in gamme and "Sol#" not in gamme:
        if freqSol >= freqSold:
            gamme.insert(4, "Sol")
        else:
            gamme.insert(5, "Sol#")
    if "Sol#" not in gamme and "La" not in gamme:
        if freqSold >= freqLa:
            gamme.insert(5, "Sol#")
        else:
            gamme.insert(5, "La")
    if "La" not in gamme and "La#" not in gamme:
        if freqLa >= freqLad:
            gamme.insert(6, "La")
        else:
            gamme.insert(6, "La#")
    if "La#" not in gamme and "Si" not in gamme:
        if freqLad >= freqSi:
            gamme.insert(6, "La#")
        else:
            gamme.insert(7, "Si")
    liste = trier(gamme)
    print(liste)
    # Comparaison afin d'avoir le taux de notes différentes de la gamme
    # On compare donc toutes les notes avec les notes de la liste (gamme)
    freqDissonnance = 0
    if "Do" not in liste:
        freqDissonnance += freqDo
    if "Do#" not in liste:
        freqDissonnance += freqDod
    if "Re" not in liste:
        freqDissonnance += freqRe
    if "Re#" not in liste:
        freqDissonnance += freqRed
    if "Mi" not in liste:
        freqDissonnance += freqMi
    if "Fa" not in liste:
        freqDissonnance += freqFa
    if "Fa#" not in liste:
        freqDissonnance += freqFad
    if "Sol" not in liste:
        freqDissonnance += freqSol
    if "Sol#" not in liste:
        freqDissonnance += freqSold
    if "La" not in liste:
        freqDissonnance += freqLa
    if "La#" not in liste:
        freqDissonnance += freqLad
    if "Si" not in liste:
        freqDissonnance += freqSi
    print ("Fréquence dissonnance : ", freqDissonnance, "%")
    #On détermine alors le nom exact de la gamme
    gamme = "Rien"
    if "Do" in liste and "Re" in liste and "Mi" in liste and "Fa" in liste and "Sol" in liste and "La" in liste and "Si" in liste:
        if freqDo > freqLa:
            gamme = "Do majeur"
        elif freqLa > freqDo:
            gamme = "La mineur"
        elif initial == 0:
            gamme = "Do majeur"
        else:
            gamme = "La mineur"
    elif "Do" in liste and "Re" in liste and "Mi" in liste and "Fa#" in liste and "Sol" in liste and "La" in liste and "Si" in liste:
        if freqSol > freqMi:
            gamme = "Sol majeur"
        elif freqMi > freqSol:
            gamme = "Mi mineur"
        elif initial == 4:
            gamme = "Mi mineur"
        else:
            gamme = "Sol majeur"
    elif "Do#" in liste and "Re" in liste and "Mi" in liste and "Fa#" in liste and "Sol" in liste and "La" in liste and "Si" in liste:
        if freqRe > freqSi:
            gamme = "Re majeur"
        elif freqSi > freqRe:
            gamme = "Si mineur"
        elif initial == 2:
            gamme = "Re majeur"
        else:
            gamme = "Si mineur"
    elif "Do#" in liste and "Re" in liste and "Mi" in liste and "Fa#" in liste and "Sol#" in liste and "La" in liste and "Si" in liste:
        if freqLa > freqFad:
            gamme = "La majeur"
        elif freqFad > freqLa:
            gamme = "Fa# mineur"
        elif initial == 9:
            gamme = "La majeur"
        else:
            gamme = "Fa# mineur"
    elif "Do#" in liste and "Re#" in liste and "Mi" in liste and "Fa#" in liste and "Sol#" in liste and "La" in liste and "Si" in liste:
        if freqMi > freqDod:
            gamme = "Mi majeur"
        elif freqDod > freqMi:
            gamme = "Do# mineur"
        elif initial == 4:
            gamme = "Mi majeur"
        else:
            gamme = "Do# mineur"
    elif "Do#" in liste and "Re#" in liste and "Mi" in liste and "Fa#" in liste and "Sol#" in liste and "La#" in liste and "Si" in liste:
        if freqSi > freqSold:
            gamme = "Si majeur"
        elif freqSold > freqSi:
            gamme = "Sol# mineur"
        elif initial == 11:
            gamme = "Si majeur"
        else:
            gamme = "Sol# mineur"
    elif "Do#" in liste and "Re#" in liste and "Fa" in liste and "Fa#" in liste and "Sol#" in liste and "La#" in liste and "Si" in liste:
        if freqFad > freqRed:
            gamme = "Fa# majeur"
        elif freqRed > freqFad:
            gamme = "Re# mineur"
        elif initial == 6:
            gamme = "Fa# majeur"
        else:
            gamme = "Re# mineur"
    elif "Do" in liste and "Do#" in liste and "Re#" in liste and "Fa" in liste and "Fa#" in liste and "Sol#" in liste and "La#" in liste:
        if freqDod > freqLad:
            gamme = "Do# majeur"
        elif freqLad > freqDod:
            gamme = "La# mineur"
        elif initial == 1:
            gamme = "Do# majeur"
        else:
            gamme = "La# mineur"
    elif "Do" in liste and "Re" in liste and "Mi" in liste and "Fa" in liste and "Sol" in liste and "La" in liste and "La#" in liste:
        if freqFa > freqRe:
            gamme = "Fa majeur"
        elif freqRe > freqFa:
            gamme = "Re mineur"
        elif initial == 5:
            gamme = "Fa majeur"
        else:
            gamme = "Re mineur"
    elif "Do" in liste and "Re" in liste and "Re#" in liste and "Fa" in liste and "Sol" in liste and "La" in liste and "La#" in liste:
        if freqLad > freqSol:
            gamme = "La# majeur"
        elif freqSol > freqLad:
            gamme = "Sol mineur"
        elif initial == 10:
            gamme = "La# majeur"
        else:
            gamme = "Sol mineur"
    elif "Do" in liste and "Re" in liste and "Re#" in liste and "Fa" in liste and "Sol" in liste and "Sol#" in liste and "La#" in liste:
        if freqRed > freqDo:
            gamme = "Re# majeur"
        elif freqDo > freqRed:
            gamme = "Do mineur"
        elif initial == 0:
            gamme = "Do mineur"
        else:
            gamme = "Re# majeur"
    elif "Do" in liste and "Do#" in liste and "Re#" in liste and "Fa" in liste and "Sol" in liste and "Sol#" in liste and "La#" in liste:
        if freqSold > freqFa:
            gamme = "Sol# majeur"
        elif freqFa > freqSold:
            gamme = "Fa mineur"
        elif initial == 5:
            gamme = "Fa mineur"
        else:
            gamme = "Sol# majeur"
    print("La gamme est :", gamme)
    return gamme


def initialisation():  # definir les différentes notes du piano (4 octaves)
    c1 = Note('C', octave=2, duration=1, volume=100)  # DO1
    c1d = Note('C#', octave=2, duration=1, volume=100)
    d1 = Note('D', octave=2, duration=1, volume=100)
    d1d = Note('D#', octave=2, duration=1, volume=100)
    e1 = Note('E', octave=2, duration=1, volume=100)
    f1 = Note('F', octave=2, duration=1, volume=100)
    f1d = Note('F#', octave=2, duration=1, volume=100)
    g1 = Note('G', octave=2, duration=1, volume=100)
    g1d = Note('G#', octave=2, duration=1, volume=100)
    a1 = Note('A', octave=2, duration=1, volume=100)
    a1d = Note('A#', octave=2, duration=1, volume=100)
    b1 = Note('B', octave=2, duration=1, volume=100)
    c2 = Note('C', octave=3, duration=1, volume=100)  # DO2
    c2d = Note('C#', octave=3, duration=1, volume=100)
    d2 = Note('D', octave=3, duration=1, volume=100)
    d2d = Note('D#', octave=3, duration=1, volume=100)
    e2 = Note('E', octave=3, duration=1, volume=100)
    f2 = Note('F', octave=3, duration=1, volume=100)
    f2d = Note('F#', octave=3, duration=1, volume=100)
    g2 = Note('G', octave=3, duration=1, volume=100)
    g2d = Note('G#', octave=3, duration=1, volume=100)
    a2 = Note('A', octave=3, duration=1, volume=100)
    a2d = Note('A#', octave=3, duration=1, volume=100)
    b2 = Note('B', octave=3, duration=1, volume=100)
    c3 = Note('C', octave=4, duration=1, volume=100)  # DO3
    c3d = Note('C#', octave=4, duration=1, volume=100)
    d3 = Note('D', octave=4, duration=1, volume=100)
    d3d = Note('D#', octave=4, duration=1, volume=100)
    e3 = Note('E', octave=4, duration=1, volume=100)
    f3 = Note('F', octave=4, duration=1, volume=100)
    f3d = Note('F#', octave=4, duration=1, volume=100)
    g3 = Note('G', octave=4, duration=1, volume=100)
    g3d = Note('G#', octave=4, duration=1, volume=100)
    a3 = Note('A', octave=4, duration=1, volume=100)
    a3d = Note('A#', octave=4, duration=1, volume=100)
    b3 = Note('B', octave=4, duration=1, volume=100)
    c4 = Note('C', octave=5, duration=1, volume=100)  # DO4
    c4d = Note('C#', octave=5, duration=1, volume=100)
    d4 = Note('D', octave=5, duration=1, volume=100)
    d4d = Note('D#', octave=5, duration=1, volume=100)
    e4 = Note('E', octave=5, duration=1, volume=100)
    f4 = Note('F', octave=5, duration=1, volume=100)
    f4d = Note('F#', octave=5, duration=1, volume=100)
    g4 = Note('G', octave=5, duration=1, volume=100)
    g4d = Note('G#', octave=5, duration=1, volume=100)
    a4 = Note('A', octave=5, duration=1, volume=100)
    a4d = Note('A#', octave=5, duration=1, volume=100)
    b4 = Note('B', octave=5, duration=1, volume=100)
    return c1, c1d, d1, d1d, e1, f1, f1d, g1, g1d, a1, a1d, b1, c2, c2d, d2, d2d, e2, f2, f2d, g2, g2d, a2, a2d, b2, \
           c3, c3d, d3, d3d, e3, f3, f3d, g3, g3d, a3, a3d, b3, c4, c4d, d4, d4d, e4, f4, f4d, g4, g4d, a4, a4d, b4


easyMIDI = EasyMIDI()
track1 = Track("acoustic grand piano")  # oops
c1, c1d, d1, d1d, e1, f1, f1d, g1, g1d, a1, a1d, b1, c2, c2d, d2, d2d, e2, f2, f2d, g2, g2d, a2, a2d, b2, c3, c3d, d3, \
d3d, e3, f3, f3d, g3, g3d, a3, a3d, b3, c4, c4d, d4, d4d, e4, f4, f4d, g4, g4d, a4, a4d, b4 = initialisation()
c = Note('C', octave=4, duration=1, volume=100)
e = Note('E', octave=4, duration=1 / 2, volume=75)
g = Note('G', octave=4, duration=1 / 3, volume=100)
# chord = Chord([c, e, g])  # a chord of notes C, E and G
track1.addNotes(
    [c1, c1d, d1, d1d, e1, f1, f1d, g1, g1d, a1, a1d, b1, c2, c2d, d2, d2d, e2, f2, f2d, g2, g2d, a2, a2d, b2, \
     c3, c3d, d3, d3d, e3, f3, f3d, g3, g3d, a3, a3d, b3, c4, c4d, d4, d4d, e4, f4, f4d, g4, g4d, a4, a4d, b4])

# roman numeral chord, first inversion (defaults to key of C)
# track1.addNotes(RomanChord('I*', octave = 5, duration = 1))

easyMIDI.addTrack(track1)
easyMIDI.writeMIDI("output.mid")

# creation de gammes
# g = Gamme()

morceau = "marcheturque.mid"
print("Morceau actuel : " , morceau)
mid = MidiFile(morceau)

notes = []
for i, track in enumerate(mid.tracks):

    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == 'note_on':
            a, b, c, d, e = str(msg).split(" ")
            g, note = str(c).split("=")
            notes.append(note)

# REGARDER LA DOC : https://mido.readthedocs.io/en/latest/index.html#

# for i in notes:
#   print(i)

gamme = detectGamme()
print("La différence entre la note la plus haute et la plus basse est :", detectRepartition())
from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=48, velocity=64, time=0))
track.append(Message('note_off', note=48, velocity=127, time=2810))

mid.save('new_song.mid')
