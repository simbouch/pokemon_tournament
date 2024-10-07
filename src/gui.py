# gui.py

import tkinter as tk
from tkinter import ttk
import random
import threading
import queue

from api import select_random_pokemons
from pokemon import Pokemon

def start_tournament():
    # Disable the start button to prevent multiple clicks
    start_button.config(state=tk.DISABLED)
    # Clear previous output
    text_output.delete('1.0', tk.END)
    # Get the number of Pokémon
    try:
        num_pokemons = int(num_pokemons_var.get())
    except ValueError:
        text_output.insert(tk.END, "Please enter a valid number for the number of Pokémon.\n")
        start_button.config(state=tk.NORMAL)
        return

    # Ensure even number
    if num_pokemons < 2:
        text_output.insert(tk.END, "Number of Pokémon must be at least 2.\n")
        start_button.config(state=tk.NORMAL)
        return
    if num_pokemons % 2 != 0:
        num_pokemons += 1
        text_output.insert(tk.END, f"Adjusted number of Pokémon to {num_pokemons} to make it even.\n")

    # Create a queue for thread-safe communication
    q = queue.Queue()
    # Start the tournament in a new thread
    threading.Thread(target=run_tournament_thread, args=(num_pokemons, q), daemon=True).start()
    # Start checking the queue
    root.after(100, check_queue, q)

def run_tournament_thread(num_pokemons, q):
    # Fetch Pokémon data
    q.put("Fetching Pokémon data...\n")
    try:
        pokemon_data_list = select_random_pokemons(num_pokemons=num_pokemons)
    except Exception as e:
        q.put(f"Error fetching Pokémon data: {e}\n")
        q.put("DONE")
        return

    # Run the tournament
    champion = run_tournament_gui(pokemon_data_list, q)
    # Announce the champion
    q.put(f"\nChampion of the Tournament: {champion.name}! 🏆\n")
    q.put("DONE")

def run_tournament_gui(pokemon_data_list, q):
    pokemons = [Pokemon(data) for data in pokemon_data_list]
    round_number = 1
    while len(pokemons) > 1:
        q.put(f"\n--- Round {round_number} ---\n")
        next_round = []
        for i in range(0, len(pokemons), 2):
            pokemon1 = pokemons[i]
            if i + 1 < len(pokemons):
                pokemon2 = pokemons[i + 1]
                winner = battle_pokemon_gui(pokemon1, pokemon2, q)
            else:
                # If odd number, pokemon1 advances automatically
                q.put(f"{pokemon1.name} advances to the next round by default.\n")
                winner = pokemon1
            next_round.append(winner)
        pokemons = next_round
        round_number += 1
    champion = pokemons[0]
    return champion

def battle_pokemon_gui(pokemon1, pokemon2, q):
    score1 = pokemon1.get_battle_score()
    score2 = pokemon2.get_battle_score()

    # Type effectiveness
    effectiveness1 = calculate_type_effectiveness(pokemon1, pokemon2)
    effectiveness2 = calculate_type_effectiveness(pokemon2, pokemon1)

    # Randomness and critical hits
    randomness1 = random.uniform(0.85, 1.0)
    critical_hit1 = 1.5 if random.random() < 0.1 else 1

    randomness2 = random.uniform(0.85, 1.0)
    critical_hit2 = 1.5 if random.random() < 0.1 else 1

    adjusted_score1 = score1 * effectiveness1 * randomness1 * critical_hit1
    adjusted_score2 = score2 * effectiveness2 * randomness2 * critical_hit2

    q.put(f"\nBattle between {pokemon1.name} and {pokemon2.name}!\n")
    q.put(f"{pokemon1.name}'s Adjusted Score: {adjusted_score1:.2f}\n")
    q.put(f"{pokemon2.name}'s Adjusted Score: {adjusted_score2:.2f}\n")

    if adjusted_score1 > adjusted_score2:
        winner = pokemon1
    elif adjusted_score2 > adjusted_score1:
        winner = pokemon2
    else:
        winner = random.choice([pokemon1, pokemon2])
        q.put("It's a tie! Winner selected at random.\n")

    q.put(f"Winner: {winner.name}\n")
    return winner

def calculate_type_effectiveness(attacking_pokemon, defending_pokemon):
    """Calculates the type effectiveness multiplier."""
    multiplier = 1.0
    for attack_type in attacking_pokemon.types:
        for defense_type in defending_pokemon.types:
            effectiveness = type_chart.get(attack_type, {}).get(defense_type, 1)
            multiplier *= effectiveness
    return multiplier

def check_queue(q):
    try:
        while True:
            msg = q.get_nowait()
            if msg == "DONE":
                start_button.config(state=tk.NORMAL)
                return
            else:
                text_output.insert(tk.END, msg)
                text_output.see(tk.END)
    except queue.Empty:
        root.after(100, check_queue, q)

# Import the type_chart
from type_chart import type_chart

# Initialize the main window
root = tk.Tk()
root.title("Pokémon Tournament Simulator")

# Create a frame for the buttons and output
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a text widget for output
text_output = tk.Text(frame, width=80, height=20)
text_output.grid(row=0, column=0, columnspan=3)

# Create a scrollbar for the text widget
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_output.yview)
scrollbar.grid(row=0, column=3, sticky=(tk.N, tk.S))
text_output['yscrollcommand'] = scrollbar.set

# Number of Pokémon Entry
num_pokemons_var = tk.StringVar(value="8")
num_pokemons_label = ttk.Label(frame, text="Number of Pokémon:")
num_pokemons_label.grid(row=1, column=0, sticky=tk.W)
num_pokemons_entry = ttk.Entry(frame, textvariable=num_pokemons_var)
num_pokemons_entry.grid(row=1, column=1, sticky=tk.W)

# Create a button to start the tournament
start_button = ttk.Button(frame, text="Start Tournament", command=start_tournament)
start_button.grid(row=1, column=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
