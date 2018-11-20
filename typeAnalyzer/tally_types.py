from api_reader import API_Reader
from game_data import getGameData

GAME_DATA = getGameData("lgp")

def extractTypes(contents):
    return contents['types']

def tallyTypes():
    api = API_Reader()
    type_data = {}

    for pokemon in GAME_DATA['pokemon']:
        data = api.get('pokemon', pokemon)
        types = extractTypes(data)
        for t in types:
            type_name = t['type']['name']
            try:
                type_data[type_name] += 1
            except KeyError:
                type_data[type_name] = 1

    return type_data

print(tallyTypes())

