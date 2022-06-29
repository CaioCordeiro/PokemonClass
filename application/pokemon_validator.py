from entities.pokemon import Pokemon

item_list = ["Leftovers", "King's Rock", "Light Ball"]
def validate_pokemon(pokemon: Pokemon):
    if not isinstance(pokemon.name, str):
        return False, "Invalid Name"
    if not isinstance(pokemon.number, int):
        return False, "Invalid Number"
    if not (isinstance(pokemon.types, list)
            and len(pokemon.types) > 0
            and len(pokemon.types) <= 2
            and all(isinstance(t, str) for t in pokemon.types)):
        return False, "Invalid Type"
    if not (isinstance(pokemon.name, str) and pokemon.item in item_list):
        return False, "Invalid Item"
    return True, "Valid Pokémon!"