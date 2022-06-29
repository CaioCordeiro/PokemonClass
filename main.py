from flask import Flask, request
from entities.pokemon import Pokemon
from application.pokemon_validator import validate_pokemon
from infrastructure.storage import PokemonStorage

app = Flask(__name__)

database = PokemonStorage()

@app.route("/pokemon", methods = ['POST'])
def create_pokemon():
    data = request.json
    new_pokemon = Pokemon(data)
    is_valid, status = validate_pokemon(new_pokemon)
    if is_valid:
        database.insert_pokemon(new_pokemon)
    code = 200 if is_valid else 418
    return "<h1>"+status+"</h1>", code

@app.route("/pokemon", methods = ['GET'])
def get_pokemons():
    return {"data": database.get_all_pokemon()}, 200

@app.route("/pokemon/search", methods = ['GET'])
def get_pokemon():
    number = int(request.args.get('number'))
    pokemon = database.get_one_pokemon(number)
    if pokemon is None:
        return "<h1>Could not find Pokémon</h1>", 418
    return {"data": pokemon}, 200

@app.route("/pokemon/search", methods = ['POST'])
def update_pokemon():
    number = int(request.args.get('number'))
    data = request.json
    new_pokemon = Pokemon(data)
    is_valid, status = validate_pokemon(new_pokemon)
    code = 200 if is_valid else 418
    if not is_valid:
        return "<h1>" + status + "<\h1>", code
    status = database.update_pokemon(number, new_pokemon)
    if status:
        return "Successfully updated Pokémon", 200
    return "Failed to update Pokémon", 418

