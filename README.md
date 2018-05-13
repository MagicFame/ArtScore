# ArtScore

Points à avancer :

- Analyse : 
    - Gamme : Fait
    - Répartition (plus haute note - plus basse note) : Fait
    - Pourcentage dissonances (notes différentes gamme) : Fait
    - Rythmique 
    - Parties qui se répètent (Organisation du morceau)
 - Analyse en masse (1000 morceaux classiques) : Fait
 - Détermination des caractéristiques de chaque style : Fait
 - Création de morceaux en semi random : Fait (changement dissonance à faire)
 - Création de morceaux chaine de markov : Fait
 - Implémentations des parties - Organisation du morceau : A réaliser
 - Implémentation de la lecture directement du fichier MIDI sur l'application : A réaliser
 - Implémentation du système de rating : A réaliser
 
IMPORTANT : 

Pour utiliser le projet sur votre interpreteur : 

- Pensez à installer les librairies suivantes : 
    - EasyMIDI : Utilisé pour créer les fichiers MIDI
    - mido : Utilisé pour analyser les fichiers MIDI
    - numpy : Utilisé pour les calculs de probabilités (Markov)
- Pensez évidemment à bien récupérer les fichiers sources (.py) et l'ensemble des fichiers du dossier "Classique"
- Vous aurez la possibilité de générer des fichiers MIDI grâce à l'application qui se créeront directement dans le repertoire principal du fichier avec pour nom : output.mid
- Afin de lire les fichiers midi, nous utilisons le logiciel MuseScore (à titre indicatif)
