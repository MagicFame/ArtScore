# ArtScore

Points à avancer :

- Analyse : 
    - Gamme : Fait
    - Répartition (plus haute note - plus basse note) : Fait
    - Pourcentage dissonances (notes différentes gamme) : Fait
    - Rythmique : Fait
    - Parties qui se répètent (Organisation du morceau)
 - Analyse en masse (1000 morceaux classiques) : Fait
 - Détermination des caractéristiques de chaque style : Fait
 - Création de morceaux en semi random : Fait
 - Création de morceaux chaine de markov : Fait
 - Implémentations des parties - Organisation du morceau : A réaliser
 - Implémentation de la lecture directement du fichier MIDI sur l'application : Fait
 - Implémentation du système de rating : A réaliser
 
IMPORTANT : 

Pour utiliser le projet sur votre interpreteur : 

- Pensez à installer les librairies suivantes : 
    - EasyMIDI : Utilisé pour créer les fichiers MIDI
    - mido : Utilisé pour analyser les fichiers MIDI
    - numpy : Utilisé pour les calculs de probabilités (Markov)
- Pensez évidemment à bien récupérer les fichiers sources (.py) et l'ensemble des fichiers du dossier "Classique" et "Jazz"
- Vous aurez la possibilité de générer des fichiers MIDI grâce à l'application qui se créeront directement dans le repertoire principal du fichier avec pour nom : random.mid et markov.mid
- Afin de lire les fichiers midi, nous utilisons le logiciel MuseScore (à titre indicatif)
