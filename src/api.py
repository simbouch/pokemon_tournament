# src/api.py

import requests  # For making HTTP requests to the PokeAPI
import random    # For generating random Pokémon IDs
import time      # For adding delays between API requests

# Base URL of the PokeAPI for Pokémon data
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon_id):
    """
    Fetches Pokémon data from PokeAPI by ID.

    Parameters:
        pokemon_id (int): The ID of the Pokémon to fetch.

    Returns:
        dict: A dictionary containing the Pokémon's data if successful.
        None: If the request fails.
    """
    try:
        # Make a GET request to the PokeAPI for the specified Pokémon ID
        response = requests.get(f"{BASE_URL}{pokemon_id}/")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()       # Return the JSON data as a Python dictionary
    except requests.exceptions.RequestException as e:
        # Print an error message if the request fails
        print(f"Error fetching data for Pokémon ID {pokemon_id}: {e}")
        return None

def select_random_pokemons(num_pokemons=16, max_pokemon_id=151):
    """
    Selects a list of unique random Pokémon IDs and fetches their data.

    Parameters:
        num_pokemons (int): The number of unique Pokémon to select.
        max_pokemon_id (int): The maximum Pokémon ID to consider.

    Returns:
        list: A list of dictionaries containing data for each selected Pokémon.
    """
    selected_pokemons = []  # List to store Pokémon data
    selected_ids = set()    # Set to keep track of selected Pokémon IDs

    # Loop until we've selected the desired number of unique Pokémon
    while len(selected_pokemons) < num_pokemons:
        # Generate a random Pokémon ID
        pokemon_id = random.randint(1, max_pokemon_id)

        # Skip if we've already selected this ID
        if pokemon_id in selected_ids:
            continue

        # Fetch the Pokémon data
        data = get_pokemon_data(pokemon_id)
        if data:
            selected_pokemons.append(data)  # Add the data to our list
            selected_ids.add(pokemon_id)    # Add the ID to our set to avoid duplicates

            # Extract the Pokémon's name
            name = data['name'].capitalize()

            # Extract the Pokémon's stats
            stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}

            # Print the Pokémon's name and stats
            print(f"Selected Pokémon: {name}")
            print("Stats:")
            for stat_name, stat_value in stats.items():
                print(f"  {stat_name.capitalize()}: {stat_value}")
            print("-" * 40)  # Separator line for readability

        # Pause to respect API rate limits
        time.sleep(0.5)

    return selected_pokemons
