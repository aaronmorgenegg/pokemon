from constants import GAME_LETS_GO_PIKACHU

def getGameData(game):
    if game.lower() in GAME_LETS_GO_PIKACHU:
        return getLetsGoPikachuGameData()

def getLetsGoPikachuGameData():
    data = {}
    pokemon = [i for i in range(1, 151)]
    pokemon.append(808)
    pokemon.append(809)
    data['pokemon'] = pokemon
    return data


