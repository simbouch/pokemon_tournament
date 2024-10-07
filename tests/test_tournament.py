# tests/test_tournament.py

import unittest
from src.tournament import run_tournament
from src.pokemon import Pokemon

class TestTournament(unittest.TestCase):
    def setUp(self):
        # Create sample Pokémon data for the tournament
        self.pokemon_data_list = []
        for i in range(1, 17):
            data = {
                'name': f'pokemon{i}',
                'id': i,
                'types': [{'type': {'name': 'type1'}}],
                'stats': [
                    {'stat': {'name': 'attack'}, 'base_stat': i * 5},
                    {'stat': {'name': 'defense'}, 'base_stat': i * 3},
                ]
            }
            self.pokemon_data_list.append(data)

    def test_run_tournament(self):
        """Test the tournament runs and returns a champion."""
        champion = run_tournament(self.pokemon_data_list)
        self.assertIsInstance(champion, Pokemon)
        # Assuming the last Pokémon has the highest stats
        self.assertEqual(champion.name, 'Pokemon16')

if __name__ == '__main__':
    unittest.main()
