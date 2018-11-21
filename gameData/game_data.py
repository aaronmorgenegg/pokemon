import pickle

from gameData.constants import FULLY_EVOLVED, GAME_LETS_GO_PIKACHU
from gameData.games.letsGoPikachu import getLetsGoPikachuGameData
from typeAnalyzer.api_reader import API_Reader


def getGameData(game):
    if game.lower() in GAME_LETS_GO_PIKACHU:
        return getLetsGoPikachuGameData()

def saveGameData(data, filename):
    with open(filename, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def loadGameData(filename):
    with open(filename, 'rb') as handle:
        data = pickle.load(handle)
        return data

def loadPokemonFromAPI(pokemon_indices):
    pokemon = []
    api = API_Reader()
    for index in pokemon_indices:
        response = api.get('pokemon', index)
        response['index'] = index
        data = loadPokemonDataFromResponse(response)
        pokemon.append(data)
    return pokemon

def loadPokemonDataFromResponse(response):
    data = {}
    data['name'] = response['name']
    data['identifier'] = response['index']
    data['types'] = loadPokemonTypesFromResponse(response)
    data['stats'] = loadPokemonStatsFromResponse(response)
    if response['index'] in FULLY_EVOLVED: data['fully_evolved'] = True
    else: data['fully_evolved'] = False
    return data

def loadPokemonTypesFromResponse(response):
    types = {}
    types.append(response['types']['0']['type']['name'])
    try:
        types.append(response['types']['1']['type']['name'])
    except KeyError:
        pass
    return types

def loadPokemonStatsFromResponse(response):
    stats = {}
    for i in range(6):
        stat_name = response['stats'][str(i)]['stat']['name']
        stats[stat_name] = response['stats'][str(i)]['base_stat']
    return stats

def addPokemonForm(pokemon, form, identifier, pokemon_data):
    for p in pokemon:
        if p.identifier == identifier:
            p.forms[form] = pokemon_data
            return
