from gameData.game_data import getGameData
from typeAnalyzer.api_reader import API_Reader

GAME_DATA = getGameData("lgp")

def tallyTypes():
    api = API_Reader()
    type_data = {}

    for pokemon in GAME_DATA['pokemon']:
        data = api.get('pokemon', pokemon)
        types = data['types']
        for t in types:
            try:
                type_data[t] += 1
            except KeyError:
                type_data[t] = 1
        for form in data['forms']:
            if form != 'partner':
                for t in form['types']:
                    try:
                        type_data[t] += 1
                    except KeyError:
                        type_data[t] = 1

    return type_data

print(tallyTypes())
