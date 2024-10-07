# src/pokemon.py

class Pokemon:
    def __init__(self, data):
        """
        Initializes a Pokemon object with data from the PokeAPI.

        Parameters:
            data (dict): A dictionary containing the Pokémon's data.
        """
        # The Pokémon's name, capitalized
        self.name = data['name'].capitalize()

        # The Pokémon's unique ID
        self.id = data['id']

        # A list of the Pokémon's types (e.g., ['grass', 'poison'])
        self.types = [t['type']['name'] for t in data['types']]

        # A dictionary of the Pokémon's stats (e.g., {'attack': 49, 'defense': 49, ...})
        self.stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}

    def get_battle_score(self):
        """
        Calculates a battle score based on all stats.

        Returns:
            int: The battle score of the Pokémon.
        """
        # Sum all the base stats
        total_score = sum(self.stats.values())
        return total_score

    def __str__(self):
        """
        Returns a string representation of the Pokémon, including stats.

        Returns:
            str: The string representation.
        """
        # Format the types as a comma-separated string
        types_str = ', '.join(self.types)

        # Format the stats
        stats_lines = [f"  {stat_name.replace('-', ' ').title()}: {stat_value}" for stat_name, stat_value in self.stats.items()]
        stats_str = '\n'.join(stats_lines)

        # Combine all parts into the final string
        return (
            f"Selected Pokémon: {self.name}\n"
            f"ID: {self.id}\n"
            f"Types: {types_str}\n"
            f"Stats:\n{stats_str}\n"
            + "-" * 40
        )
