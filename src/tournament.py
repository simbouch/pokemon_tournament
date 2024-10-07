# tournament.py

from battle import battle_pokemon

def run_tournament(pokemons):
    """Runs the tournament and returns the champion."""
    round_number = 1
    current_pokemons = pokemons.copy()
    while len(current_pokemons) > 1:
        print(f"\n--- Round {round_number} ---")
        next_round = []
        for i in range(0, len(current_pokemons), 2):
            pokemon1 = current_pokemons[i]
            if i + 1 < len(current_pokemons):
                pokemon2 = current_pokemons[i + 1]
                winner = battle_pokemon(pokemon1, pokemon2)
            else:
                # If odd number, pokemon1 advances automatically
                print(f"{pokemon1.name} advances to the next round by default.")
                winner = pokemon1
            next_round.append(winner)
        current_pokemons = next_round
        round_number += 1

    champion = current_pokemons[0]
    print(f"\nChampion of the Tournament: {champion.name}! 🏆")
    return champion
