****************************Pokémon Tournament Simulator**************************

Welcome to the Pokémon Tournament Simulator! This project is a Python application that simulates 
a tournament between 4 to 16 randomly selected Pokémon using data from the PokeAPI. The program fetches 
Pokémon data, organizes battles based on their stats, and determines 
champion through elimination rounds.

***************Table of Contents*************

Features
Requirements
Installation
Usage
Command-Line Interface
Graphical User Interface

****Features
API Integration: Fetches real-time Pokémon data from the PokeAPI.
Battle Simulation:Simulates battles based on Pokémon stats (attack and defense).
Tournament Organization: Manages an elimination-style tournament until a champion is crowned.
Graphical User Interface: Provides a simple GUI using Tkinter.
Unit Testing: Includes tests to ensure code reliability and correctness.

src/: Contains all source code modules.
main.py: Entry point of the application.
api.py: Handles API requests to the PokeAPI.
pokemon.py: Defines the Pokemon class.
battle.py: Contains the battle logic between two Pokémon.
tournament.py: Manages the tournament flow.
gui.py: Provides a simple GUI using Tkinter.
tests/: Contains unit tests for the project modules.

*****Requirements

Python 3.6 or higher
Python Packages
requests==2.31.0
tkinter (included with most Python installations)
unittest (included with the Python standard library)

*****Installation


Clone the repository:

git clone https://github.com/simbouch/pokemon_tournament.git
python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate


Install the required packages:

pip install -r requirements.txt


*****Usage


You can run the application in two modes: Command-Line Interface (CLI) or Graphical User Interface (GUI).

*****Command-Line Interface

Navigate to the src/ directory:
cd src
Run the main script:

python main.py

Watch the tournament unfold in your terminal!

*****Graphical User Interface

Ensure you are in the project's root directory.

Run the main script:
python src/main.py
A window titled "Pokémon Tournament Simulator" will appear.
Click the "Start Tournament" button to begin the simulation.

