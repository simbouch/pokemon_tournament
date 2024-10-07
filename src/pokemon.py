# src/pokemon.py

class Pokemon:
    def __init__(self, data):
        self.name = data['name'].capitalize()
        self.id = data['id']
        self.types = [t['type']['name'] for t in data['types']]
        self.stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}

    def get_battle_score(self):
        """Calculates a battle score based on attack and defense stats."""
        attack = self.stats.get('attack', 0)
        defense = self.stats.get('defense', 0)
        return attack + defense

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Types: {', '.join(self.types)})"
