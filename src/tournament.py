# src/tournament.py

from pokemon import Pokemon  # Import the Pokemon class from the pokemon module
from battle import battle_pokemon  # Import the battle_pokemon function from the battle module

def run_tournament(pokemon_data_list):
    """Runs the tournament and returns the champion."""
    # Create Pokemon objects from the provided data list
    pokemons = [Pokemon(data) for data in pokemon_data_list]

    round_number = 1  # Initialize the round counter
    # Continue the tournament until only one Pokémon remains
    while len(pokemons) > 1:
        print(f"\n--- Round {round_number} ---")
        next_round = []  # List to store winners advancing to the next round
        # Iterate over the pokemons list in steps of 2 to get battle pairs
        for i in range(0, len(pokemons), 2):
            pokemon1 = pokemons[i]  # First Pokémon in the pair
            pokemon2 = pokemons[i + 1]  # Second Pokémon in the pair
            # Simulate a battle between the two Pokémon
            winner = battle_pokemon(pokemon1, pokemon2)
            next_round.append(winner)  # Add the winner to the next round
        pokemons = next_round  # Update the pokemons list with winners
        round_number += 1  # Increment the round number

    # The last remaining Pokémon is the champion
    champion = pokemons[0]
    print(f"\nChampion of the Tournament: {champion.name}! 🏆")
    return champion  # Return the champion Pokémon
