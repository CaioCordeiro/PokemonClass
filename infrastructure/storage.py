from entities.pokemon import Pokemon

class PokemonStorage:
    def __init__(self):
        self.storage = []

    def insert_pokemon(self, pokemon: Pokemon):
        self.storage.append(pokemon)
        return "Pokémon successfully added"

    def get_all_pokemon(self):
        return [pokemon.to_dict() for pokemon in self.storage]

    def get_one_pokemon(self, number):
        for pokemon in self.storage:
            if pokemon.number == number:
                return pokemon.to_dict()
        return None

    def update_pokemon(self, number, new_pokemon):
        for idx, pokemon in enumerate(self.storage):
            if pokemon.number == number:
                self.storage[idx] = new_pokemon
                return True
        return False

