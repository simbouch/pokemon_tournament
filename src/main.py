# src/main.py

from src.api import select_random_pokemons
from src.tournament import run_tournament


def main():
    print("Welcome to the Pokémon Tournament Simulator!\n")
    selected_pokemon_data = select_random_pokemons()
    champion = run_tournament(selected_pokemon_data)
    print(f"\nCongratulations to {champion.name} for winning the tournament!")

if __name__ == "__main__":
    main()
