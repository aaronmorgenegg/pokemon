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
    geodude_data = {}
    geodude_data['identifier'] = 74
    geodude_data['name'] = 'geodude-alola'
    geodude_data['stats'] = {
            'speed': 20,
            'special-defense': 30,
            'special-attack': 30,
            'defense': 100,
            'attack': 80,
            'hp': 40
            }
    geodude_data['types'] = ['rock', 'electric']
    geodude_data['fully_evolved'] = False

    geodude = Pokemon(geodude_data)
    game_data.addPokemonForm(pokemon, 'alola', 74, geodude)
    # golem
    golem_data = {}
    golem_data['identifier'] = 76
    golem_data['name'] = 'golem-alola'
    golem_data['stats'] = {
            'speed': 45,
            'special-defense': 65,
            'special-attack': 55,
            'defense': 130,
            'attack': 120,
            'hp': 80
            }
    golem_data['types'] = ['rock', 'electric']
    golem_data['fully_evolved'] = True

    golem = Pokemon(golem_data)
    game_data.addPokemonForm(pokemon, 'alola', 76, golem)
    # graveler
    graveler_data = {}
    graveler_data['identifier'] = 75
    graveler_data['name'] = 'graveler-alola'
    graveler_data['stats'] = {
            'speed': 35,
            'special-defense': 45,
            'special-attack': 45,
            'defense': 115,
            'attack': 95,
            'hp': 55
            }
    graveler_data['types'] = ['rock', 'electric']
    graveler_data['fully_evolved'] = False

    graveler = Pokemon(graveler_data)
    game_data.addPokemonForm(pokemon, 'alola', 75, graveler)
    # grimer
    grimer_data = {}
    grimer_data['identifier'] = 88
    grimer_data['name'] = 'grimer-alola'
    grimer_data['stats'] = {
            'speed': 25,
            'special-defense': 50,
            'special-attack': 40,
            'defense': 50,
            'attack': 80,
            'hp': 80
            }
    grimer_data['types'] = ['poison', 'dark']
    grimer_data['fully_evolved'] = False

    grimer = Pokemon(grimer_data)
    game_data.addPokemonForm(pokemon, 'alola', 88, grimer)
    # marowak
    marowak_data = {}
    marowak_data['identifier'] = 105
    marowak_data['name'] = 'marowak-alola'
    marowak_data['stats'] = {
            'speed': 45,
            'special-defense': 80,
            'special-attack': 50,
            'defense': 110,
            'attack': 80,
            'hp': 60
            }
    marowak_data['types'] = ['fire', 'ghost']
    marowak_data['fully_evolved'] = True

    marowak = Pokemon(marowak_data)
    game_data.addPokemonForm(pokemon, 'alola', 105, marowak)
    # meowth
    meowth_data = {}
    meowth_data['identifier'] = 52
    meowth_data['name'] = 'meowth-alola'
    meowth_data['stats'] = {
            'speed': 90,
            'special-defense': 40,
            'special-attack': 50,
            'defense': 35,
            'attack': 35,
            'hp': 40
            }
    meowth_data['types'] = ['dark']
    meowth_data['fully_evolved'] = False

    meowth = Pokemon(meowth_data)
    game_data.addPokemonForm(pokemon, 'alola', 52, meowth)
    # muk
    muk_data = {}
    muk_data['identifier'] = 89
    muk_data['name'] = 'muk-alola'
    muk_data['stats'] = {
            'speed': 50,
            'special-defense': 100,
            'special-attack': 65,
            'defense': 75,
            'attack': 105,
            'hp': 105
            }
    muk_data['types'] = ['poison', 'dark']
    muk_data['fully_evolved'] = True

    muk = Pokemon(muk_data)
    game_data.addPokemonForm(pokemon, 'alola', 89, muk)
    # ninetales
    ninetales_data = {}
    ninetales_data['identifier'] = 38
    ninetales_data['name'] = 'ninetales-alola'
    ninetales_data['stats'] = {
            'speed': 109,
            'special-defense': 100,
            'special-attack': 81,
            'defense': 75,
            'attack': 67,
            'hp': 73
            }
    ninetales_data['types'] = ['ice', 'fairy']
    ninetales_data['fully_evolved'] = True

    ninetales = Pokemon(ninetales_data)
    game_data.addPokemonForm(pokemon, 'partner', 38, ninetales)
    # persian
    persian_data = {}
    persian_data['identifier'] = 53
    persian_data['name'] = 'persian-alola'
    persian_data['stats'] = {
            'speed': 115,
            'special-defense': 65,
            'special-attack': 75,
            'defense': 60,
            'attack': 60,
            'hp': 65
            }
    persian_data['types'] = ['dark']
    persian_data['fully_evolved'] = True

    persian = Pokemon(persian_data)
    game_data.addPokemonForm(pokemon, 'alola', 53, persian)
    # raichu
    raichu_data = {}
    raichu_data['identifier'] = 26
    raichu_data['name'] = 'raichu-alola'
    raichu_data['stats'] = {
            'speed': 110,
            'special-defense': 85,
            'special-attack': 95,
            'defense': 50,
            'attack': 85,
            'hp': 60
            }
    raichu_data['types'] = ['electric', 'psychic']
    raichu_data['fully_evolved'] = True

    raichu = Pokemon(raichu_data)
    game_data.addPokemonForm(pokemon, 'alola', 26, raichu)
    # raticate
    raticate_data = {}
    raticate_data['identifier'] = 20
    raticate_data['name'] = 'raticate-alola'
    raticate_data['stats'] = {
            'speed': 77,
            'special-defense': 80,
            'special-attack': 40,
            'defense': 70,
            'attack': 71,
            'hp': 75
            }
    raticate_data['types'] = ['normal', 'dark']
    raticate_data['fully_evolved'] = True

    raticate = Pokemon(raticate_data)
    game_data.addPokemonForm(pokemon, 'alola', 20, raticate)
    # rattata
    rattata_data = {}
    rattata_data['identifier'] = 19
    rattata_data['name'] = 'rattata-alola'
    rattata_data['stats'] = {
            'speed': 72,
            'special-defense': 35,
            'special-attack': 25,
            'defense': 35,
            'attack': 56,
            'hp': 30
            }
    rattata_data['types'] = ['normal', 'dark']
    rattata_data['fully_evolved'] = False

    rattata = Pokemon(rattata_data)
    game_data.addPokemonForm(pokemon, 'alola', 19, rattata)
    # sandshrew
    sandshrew_data = {}
    sandshrew_data['identifier'] = 27
    sandshrew_data['name'] = 'sandshrew-alola'
    sandshrew_data['stats'] = {
            'speed': 40,
            'special-defense': 35,
            'special-attack': 10,
            'defense': 90,
            'attack': 75,
            'hp': 50
            }
    sandshrew_data['types'] = ['ice', 'steel']
    sandshrew_data['fully_evolved'] = False

    sandshrew = Pokemon(sandshrew_data)
    game_data.addPokemonForm(pokemon, 'alola', 27, sandshrew)
    # sandslash
    sandslash_data = {}
    sandslash_data['identifier'] = 28
    sandslash_data['name'] = 'sandslash-alola'
    sandslash_data['stats'] = {
            'speed': 65,
            'special-defense': 65,
            'special-attack': 25,
            'defense': 120,
            'attack': 100,
            'hp': 75
            }
    sandslash_data['types'] = ['ice', 'steel']
    sandslash_data['fully_evolved'] = True

    sandslash = Pokemon(sandslash_data)
    game_data.addPokemonForm(pokemon, 'alola', 28, sandslash)
    # vulpix
    vulpix_data = {}
    vulpix_data['identifier'] = 37
    vulpix_data['name'] = 'vulpix-alola'
    vulpix_data['stats'] = {
            'speed': 65,
            'special-defense': 65,
            'special-attack': 50,
            'defense': 40,
            'attack': 41,
            'hp': 38
            }
    vulpix_data['types'] = ['ice']
    vulpix_data['fully_evolved'] = False

    vulpix = Pokemon(vulpix_data)
    game_data.addPokemonForm(pokemon, 'alola', 37, vulpix)

def addMegaPokemon(pokemon):
    # TODO
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
