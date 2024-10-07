# tests/test_api.py

import unittest
from src.api import get_pokemon_data, select_random_pokemons

class TestAPI(unittest.TestCase):
    def test_get_pokemon_data_valid_id(self):
        """Test fetching data for a valid Pokémon ID."""
        data = get_pokemon_data(1)  # Bulbasaur
        self.assertIsNotNone(data)
        self.assertEqual(data['name'], 'bulbasaur')

    def test_get_pokemon_data_invalid_id(self):
        """Test fetching data for an invalid Pokémon ID."""
        data = get_pokemon_data(-1)  # Invalid ID
        self.assertIsNone(data)

    def test_select_random_pokemons(self):
        """Test selecting a specific number of random Pokémon."""
        pokemons = select_random_pokemons(num_pokemons=5)
        self.assertEqual(len(pokemons), 5)
        for pokemon in pokemons:
            self.assertIn('name', pokemon)
            self.assertIn('stats', pokemon)

if __name__ == '__main__':
    unittest.main()
