import MarkovGen as MarkovGen
from EasyMIDI import EasyMIDI, Track, Note, Chord, RomanChord
from random import choice
import mido
from mido import MidiFile
import Gamme
from math import *
from tkinter import *
from AleatoireGen import AleatoireGen
from Genre import Genre
from MarkovGen import MarkovGen
import pygame
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
    classique.addRepartition(haute - basse)
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
    print("Fréquence dissonnance : ", freqDissonnance, "%")
    classique.addDissonance(freqDissonnance)
    # On détermine alors le nom exact de la gamme
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
    classique.addGamme(gamme)
    return gamme

def detectMarkov():
    cpt = 0

    for cpt in range(len(notes) - 1):
        if 48 <= int(notes[cpt]) <= 83 and 48 <= int(notes[cpt + 1]) <= 83 and notes[cpt] != notes[cpt+1]:  # notes faisant partie de la création
            markov[int(notes[cpt]) - 48][int(notes[cpt + 1]) - 48] += 1

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print ("Music file %s loaded!" % music_file)
    except pygame.error:
        print ("File %s not found! (%s)" % (music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
methodeGeneree = "Aucune"

def generer(methode):
    bottom.pack(padx=30, pady=30)
    valider.config(state=NORMAL)
    global methodeGeneree
    methodeGeneree = methode
    # ---> A PARTIR D'ICI VA VERS algo de generation en fonction de la methode
    if methodeGeneree == "aleatoire":
        Generation = AleatoireGen(classique)
        pygame.mixer.music.load("random.mid")
        pygame.mixer.music.play()
    elif methodeGeneree == "markov":
        Markov = MarkovGen(classique, markov)
        pygame.mixer.music.load("markov.mid")
        pygame.mixer.music.play()
def noter():
    valider.config(state=DISABLED)
    # pour chaque génération on ne peut donner qu'une seule note
    print(methodeGeneree)
    gamme = int(gamme_s.get())
    rythme = int(rythme_s.get())
    orga = int(orga_s.get())
    print("Note sur la gamme " + str(gamme))
    print("Note sur le rythme "+ str(rythme))
    print("Note sur l'organisation du morceau " + str(orga))
    # ---> A PARTIR D'ICI VA VERS attribution des notes en fonction de la méthodeGénérée

# fenêtre principale
fenetre = Tk()
fenetre.title("ArtScore")
titre = Label(fenetre, text="ArtScore")
titre.pack()


easyMIDI = EasyMIDI()
track1 = Track("acoustic grand piano")  # oops


compt = 0

markov = []  # tableau de markov
for i in range(36):
    markov.append([0] * 36)
classique = Genre("Classique")
for compt in range(1, 360):

    morceau = "n (" + str(compt) + ").mid"
    path = "Classique/" + morceau
    print("Morceau actuel :", path)
    mid = MidiFile(path)

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
    detectMarkov()
    gamme = detectGamme()
    print("La différence entre la note la plus haute et la plus basse est :", detectRepartition())


classique.afficherInfoGenre()
for i in range(36):
    print(i, "|", markov[i])
pygame.init()



# cadre du haut (choix de la méthode)
cadre = Frame(fenetre, width=768, height=576, borderwidth=2, relief=GROOVE)
cadre.pack(padx=30, pady=30)
label = Label(cadre, text="Méthodes de génération de musiques :")
label.pack(padx=10, pady=10)
Button(cadre, text='Aléatoire', command=lambda: generer('aleatoire'), padx=10, pady=5).pack(side=LEFT, padx=50, pady=20)
Button(cadre, text='Chaînes de Markov', command=lambda: generer('markov'), padx=10, pady=5).pack(side=RIGHT, padx=50, pady=20)

# cadre du bas (notes)
bottom = Frame(fenetre, borderwidth=2, relief=GROOVE)
labelbottom = Label(bottom, text="Écoutez le morceau puis donnez votre avis :")
labelbottom.pack(padx=10, pady=10)
gamme_s = Spinbox(bottom, from_=0, to=5)
Label(bottom, text="Gamme :").pack(pady=5)
gamme_s.pack()
rythme_s = Spinbox(bottom, from_=0, to=5)
Label(bottom, text="Rythmique :").pack(pady=5)
rythme_s.pack()
orga_s = Spinbox(bottom, from_=0, to=5)
Label(bottom, text="Organisation du morceau :").pack(pady=5)
orga_s.pack()
valider = Button(bottom, text='Valider', command=noter, padx=10, pady=5)
valider.pack(padx=50, pady=20)
fenetre.mainloop()





