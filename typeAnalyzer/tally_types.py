from gameData.constants import GAME_LETS_GO_PIKACHU
from gameData.game_data import getGameData
from typeAnalyzer.api_reader import API_Reader

GAME_DATA = getGameData(GAME_LETS_GO_PIKACHU)

def tallyTypes():
    type_data = {}

    for pokemon in GAME_DATA['pokemon']:
        types = pokemon.types
        for t in types:
            try:
                type_data[t] += 1
            except KeyError:
                type_data[t] = 1
        for form, value in pokemon.forms.items():
            if form != 'partner':
                for t in value.types:
                    try:
                        type_data[t] += 1
                    except KeyError:
                        type_data[t] = 1

    return type_data

print(tallyTypes())
