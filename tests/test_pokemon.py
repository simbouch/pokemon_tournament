# tests/test_pokemon.py

import unittest
from src.pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            'name': 'bulbasaur',
            'id': 1,
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [
                {'stat': {'name': 'attack'}, 'base_stat': 49},
                {'stat': {'name': 'defense'}, 'base_stat': 49},
                # Include other stats if necessary
            ]
        }
        self.pokemon = Pokemon(self.sample_data)

    def test_pokemon_initialization(self):
        """Test if the Pokémon object initializes correctly."""
        self.assertEqual(self.pokemon.name, 'Bulbasaur')
        self.assertEqual(self.pokemon.id, 1)
        self.assertEqual(self.pokemon.types, ['grass', 'poison'])
        self.assertEqual(self.pokemon.stats['attack'], 49)
        self.assertEqual(self.pokemon.stats['defense'], 49)

    def test_get_battle_score(self):
        """Test the battle score calculation."""
        expected_score = 49 + 49  # attack + defense
        self.assertEqual(self.pokemon.get_battle_score(), expected_score)

if __name__ == '__main__':
    unittest.main()
