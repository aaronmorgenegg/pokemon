from gameData.constants import GAME_LETS_GO_PIKACHU
from gameData.game_data import getGameData
from pokemon.pokedex import Pokedex
from typeAnalyzer.type_analyzer import TypeAnalyzer


# POKEDEX = Pokedex(getGameData(GAME_LETS_GO_PIKACHU))
#
# print(POKEDEX.tallyTypes())

print(TypeAnalyzer.analyze(['ground', 'water']))
