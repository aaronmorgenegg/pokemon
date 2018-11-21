from gameData import game_data
from gameData.constants import GAME_LETS_GO_PIKACHU
from pokemon.pokemon import Pokemon
from typeAnalyzer.constants import VERBOSITY


def getLetsGoPikachuGameData():
    try:
        if VERBOSITY >=2: print("Loading cached data from {}.pickle".format(GAME_LETS_GO_PIKACHU))
        return game_data.loadGameData("{}.pickle".format(GAME_LETS_GO_PIKACHU))
    except FileNotFoundError:
        if VERBOSITY >=2: print("Cached data not found. Retrieving data from PokeAPI".format(GAME_LETS_GO_PIKACHU))
        data = {}
        data['pokemon'] = getLetsGoPikachuPokemonData()
        game_data.saveGameData(data, "{}.pickle".format(GAME_LETS_GO_PIKACHU))
        return data

def getLetsGoPikachuPokemonData():
    pokemon_indices = [i for i in range(1, 151)]
    pokemon = game_data.loadPokemonFromAPI(pokemon_indices)

    addPartnerPokemon(pokemon)
    addAlolaPokemon(pokemon)
    addMegaPokemon(pokemon)
    addMeltan(pokemon)

    return pokemon

def addPartnerPokemon(pokemon):
    # TODO(optional) add partner eevee
    partner_pikachu_data = {}
    partner_pikachu_data['identifier'] = 25
    partner_pikachu_data['name'] = 'pikachu-partner'
    partner_pikachu_data['stats'] = {
            'speed': 120,
            'special-defense': 60,
            'special-attack': 75,
            'defense': 50,
            'attack': 80,
            'hp': 45
            }
    partner_pikachu_data['types'] = ['electric']
    partner_pikachu_data['fully_evolved'] = True

    partner_pikachu = Pokemon(partner_pikachu_data)
    game_data.addPokemonForm(pokemon, 'partner', 25, partner_pikachu)

def addAlolaPokemon(pokemon):
    # diglett
    diglett_data = {}
    diglett_data['identifier'] = 50
    diglett_data['name'] = 'diglett-alola'
    diglett_data['stats'] = {
            'speed': 90,
            'special-defense': 45,
            'special-attack': 35,
            'defense': 30,
            'attack': 55,
            'hp': 10
            }
    diglett_data['types'] = ['ground', 'steel']
    diglett_data['fully_evolved'] = False

    diglett = Pokemon(diglett_data)
    game_data.addPokemonForm(pokemon, 'alola', 50, diglett)
    # dugtrio
    dugtrio_data = {}
    dugtrio_data['identifier'] = 51
    dugtrio_data['name'] = 'dugtrio-alola'
    dugtrio_data['stats'] = {
            'speed': 110,
            'special-defense': 70,
            'special-attack': 50,
            'defense': 60,
            'attack': 100,
            'hp': 35
            }
    dugtrio_data['types'] = ['ground', 'steel']
    dugtrio_data['fully_evolved'] = False

    dugtrio = Pokemon(dugtrio_data)
    game_data.addPokemonForm(pokemon, 'alola', 51, dugtrio)
    # exeggutor
    exeggutor_data = {}
    exeggutor_data['identifier'] = 103
    exeggutor_data['name'] = 'exeggutor-alola'
    exeggutor_data['stats'] = {
            'speed': 45,
            'special-defense': 75,
            'special-attack': 125,
            'defense': 85,
            'attack': 105,
            'hp': 95
            }
    exeggutor_data['types'] = ['grass','dragon']
    exeggutor_data['fully_evolved'] = True

    exeggutor = Pokemon(exeggutor_data)
    game_data.addPokemonForm(pokemon, 'alola', 103, exeggutor)
    # geodude
    # golem
    # graveler
    # grimer
    # marowak
    # meowth
    # muk
    # ninetales
    # persian
    # raichu
    # raticate
    # ratata
    # sandshrew
    # sandslash
    # vulpix

def addMegaPokemon(pokemon):
    pass

def addMeltan(pokemon):
    meltan_data = {}
    meltan_data['identifier'] = 808
    meltan_data['name'] = 'meltan'
    meltan_data['stats'] = {
            'speed': 34,
            'special-defense': 35,
            'special-attack': 55,
            'defense': 65,
            'attack': 65,
            'hp': 46
            }
    meltan_data['types'] = ['steel']
    meltan_data['fully_evolved'] = False

    meltitan_data = {}
    meltitan_data['identifier'] = 809
    meltitan_data['name'] = 'meltitan'
    meltitan_data['stats'] = {
            'speed': 34,
            'special-defense': 65,
            'special-attack': 80,
            'defense': 143,
            'attack': 143,
            'hp': 135
            }
    meltitan_data['types'] = ['steel']
    meltitan_data['fully_evolved'] = True

    meltan = Pokemon(meltan_data)
    meltitan = Pokemon(meltitan_data)

    pokemon.append(meltan)
    pokemon.append(meltitan)
