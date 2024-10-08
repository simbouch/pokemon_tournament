****************************Simulateur de Tournoi Pokémon**************************

Ce projet est une application Python qui simule un tournoi entre 4 à 16 Pokémon sélectionnés aléatoirement en utilisant les données de la PokeAPI. Le programme récupère les données des Pokémon, organise des combats en fonction de leurs statistiques et détermine le champion à travers des rondes d'élimination.

***************Table des Matières*************

Fonctionnalités
Exigences
Installation
Utilisation
Interface en Ligne de Commande
Interface Graphique Utilisateur

****Fonctionnalités

Intégration API : Récupère les données Pokémon en temps réel depuis la PokeAPI.
Simulation de Combat : Simule des combats basés sur les statistiques des Pokémon (attaque et défense).
Organisation du Tournoi : Gère un tournoi de style élimination jusqu'à ce qu'un champion soit couronné.
Interface Graphique Utilisateur : Fournit une interface graphique simple utilisant Tkinter.
Tests Unitaires : Inclut des tests pour garantir la fiabilité et la précision du code.

****Structure du Projet

src/ : Contient tous les modules de code source.
main.py : Point d'entrée de l'application.
api.py : Gère les requêtes API vers la PokeAPI.
pokemon.py : Définit la classe Pokémon.
battle.py : Contient la logique des combats entre deux Pokémon.
tournament.py : Gère le déroulement du tournoi.
gui.py : Fournit une interface graphique simple utilisant Tkinter.
tests/ : Contient les tests unitaires pour les modules du projet.

**** Exigences
Python 3.6 ou supérieur
Paquets Python
requests==2.31.0
tkinter (inclus avec la plupart des installations Python)
unittest (inclus dans la bibliothèque standard de Python)

*****Installation


Cloner le dépôt:

git clone https://github.com/simbouch/pokemon_tournament.git
python -m venv venv
Créer un environnement virtuel:

sur  Windows:

venv\Scripts\activate

sur macOS/Linux:

source venv/bin/activate


Installer les paquets requis:

pip install -r requirements.txt


****Utilisation


Vous pouvez exécuter l'application en deux modes : Interface en Ligne de Commande (CLI) ou Interface Graphique Utilisateur (GUI).

****Interface en Ligne de Commande


Naviguer vers le répertoire src/ :
cd src

Exécuter le script principal ::

python main.py

Watch the tournament unfold in your terminal!

*****Interface Graphique Utilisateur

Naviguer vers le répertoire src/ :
cd src

Exécuter le script de l'interface graphique :
python src/main.py

Cela ouvrira une fenêtre graphique où vous pourrez démarrer le tournoi Pokémon en entrant le nombre de Pokémon souhaité.
Cliquez sur le bouton « Démarrer le tournoi » pour commencer la simulation.

