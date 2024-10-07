# tests/test_battle.py

import unittest
from src.pokemon import Pokemon
from src.battle import battle_pokemon

class TestBattle(unittest.TestCase):
    def setUp(self):
        data1 = {
            'name': 'bulbasaur',
            'id': 1,
            'types': [{'type': {'name': 'grass'}}],
            'stats': [
                {'stat': {'name': 'attack'}, 'base_stat': 49},
                {'stat': {'name': 'defense'}, 'base_stat': 49},
            ]
        }
        data2 = {
            'name': 'charmander',
            'id': 4,
            'types': [{'type': {'name': 'fire'}}],
            'stats': [
                {'stat': {'name': 'attack'}, 'base_stat': 52},
                {'stat': {'name': 'defense'}, 'base_stat': 43},
            ]
        }
        self.pokemon1 = Pokemon(data1)
        self.pokemon2 = Pokemon(data2)

    def test_battle_pokemon(self):
        """Test the battle between two Pokémon."""
        winner = battle_pokemon(self.pokemon1, self.pokemon2)
        self.assertEqual(winner.name, 'Charmander')

    def test_battle_pokemon_tie(self):
        """Test the battle outcome when there is a tie."""
        # Modify stats to create a tie
        self.pokemon1.stats['attack'] = 50
        self.pokemon1.stats['defense'] = 50
        self.pokemon2.stats['attack'] = 50
        self.pokemon2.stats['defense'] = 50

        winners = set()
        # Run multiple times to check random selection
        for _ in range(10):
            winner = battle_pokemon(self.pokemon1, self.pokemon2)
            winners.add(winner.name)
        self.assertEqual(winners, {'Bulbasaur', 'Charmander'})

if __name__ == '__main__':
    unittest.main()

