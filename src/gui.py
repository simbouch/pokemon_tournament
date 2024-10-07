# src/gui.py

import tkinter as tk
from tkinter import ttk
import random

from api import select_random_pokemons
from pokemon import Pokemon

def start_tournament():
    # Clear previous output
    text_output.delete('1.0', tk.END)
    
    # Select Pokémon data
    pokemon_data_list = select_random_pokemons()
    
    # Run the tournament and capture output
    champion = run_tournament_gui(pokemon_data_list)
    
    # Display the champion
    text_output.insert(tk.END, f"\nChampion of the Tournament: {champion.name}! 🏆\n")

def run_tournament_gui(pokemon_data_list):
    pokemons = [Pokemon(data) for data in pokemon_data_list]
    round_number = 1
    while len(pokemons) > 1:
        text_output.insert(tk.END, f"\n--- Round {round_number} ---\n")
        root.update()
        next_round = []
        for i in range(0, len(pokemons), 2):
            pokemon1 = pokemons[i]
            pokemon2 = pokemons[i + 1]
            winner = battle_pokemon_gui(pokemon1, pokemon2)
            next_round.append(winner)
        pokemons = next_round
        round_number += 1
    champion = pokemons[0]
    return champion

def battle_pokemon_gui(pokemon1, pokemon2):
    score1 = pokemon1.get_battle_score()
    score2 = pokemon2.get_battle_score()
    
    text_output.insert(tk.END, f"\nBattle between {pokemon1.name} and {pokemon2.name}!\n")
    text_output.insert(tk.END, f"{pokemon1.name}'s Score: {score1}\n")
    text_output.insert(tk.END, f"{pokemon2.name}'s Score: {score2}\n")
    root.update()
    
    if score1 > score2:
        winner = pokemon1
    elif score2 > score1:
        winner = pokemon2
    else:
        winner = random.choice([pokemon1, pokemon2])
        text_output.insert(tk.END, "It's a tie! Winner selected at random.\n")
    
    text_output.insert(tk.END, f"Winner: {winner.name}\n")
    root.update()
    return winner

# Initialize the main window
root = tk.Tk()
root.title("Pokémon Tournament Simulator")

# Create a frame for the buttons and output
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a text widget for output
text_output = tk.Text(frame, width=80, height=20)
text_output.grid(row=0, column=0, columnspan=2)

# Create a scrollbar for the text widget
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_output.yview)
scrollbar.grid(row=0, column=2, sticky=(tk.N, tk.S))
text_output['yscrollcommand'] = scrollbar.set

# Create a button to start the tournament
start_button = ttk.Button(frame, text="Start Tournament", command=start_tournament)
start_button.grid(row=1, column=0, pady=10)

# Start the Tkinter event loop
root.mainloop()
