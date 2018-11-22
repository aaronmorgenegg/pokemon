import pickle

from typeAnalyzer.constants import TYPES
from typeAnalyzer.type_analyzer import TypeAnalyzer


class Pokedex:
    """Contains a list of pokemon, and operations on those pokemon"""
    def __init__(self, data):
        self.pokemon = data['pokemon']
        self.stats_stats = {}

    def computeTypeStats(self):
        try:
            return self.type_stats
        except AttributeError:
            self.type_stats = {}
            for type in TYPES:
                self.type_stats[type] = {'count': 0, 'defense': 0, 'attack': 0}

            self.tallyTypes()
            # self._computeTypeRatings # TODO compute the offensive and defensive ratings for each type,
            # TODO, based on the effectiveness to other types, and how many pokemon are resistant/weak to that type

            return self.type_stats

    def tallyTypes(self):
        for pokemon in self.pokemon:
            types = pokemon.types
            for t in types:
                self.type_stats[t]['count'] += 1
            for form, value in pokemon.forms.items():
                if form != 'partner':
                    for t in value.types:
                        self.type_stats[t]['count'] += 1

    def computeStatsStats(self):
        """Compute various statistics(average, std dev) about pokemon stats(hp, attack etc)"""
        if len(self.stats_stats) == 0:
            self.stats_stats = {'stats':{
                                    'hp':{'total':0, 'values':[]},
                                    'attack':{'total':0, 'values':[]},
                                    'defense':{'total':0, 'values':[]},
                                    'special-attack':{'total':0, 'values':[]},
                                    'special-defense':{'total':0, 'values':[]},
                                    'speed':{'total':0, 'values':[]}
                                    },
                                'count':0}

            self._computeStatTotals()
            self._computeStatAverages()

            return self.stats_stats
        else:
            return self.stats_stats

    def getPokemon(self, key):
        """Get pokemon by key(id or name)"""
        if type(key) == str:
            # pokemon name
            for pokemon in self.pokemon:
                if pokemon.name == key:
                    return pokemon
                for form, value in pokemon.forms.items():
                    if value.name == key:
                        return value
        if type(key) == int:
            # pokemon id
            for pokemon in self.pokemon:
                if pokemon.identifier == key:
                    return pokemon
                for form, value in pokemon.forms.items():
                    if value.identifier == key:
                        return value
        raise IndexError('Pokemon not fond by key {}'.format(key))

    def rateStats(self, pokemon_key):
        self.computeStatsStats()
        self.computeTypeStats()
        pokemon = self.getPokemon(pokemon_key)
        stat_ratings = {}
        for stat, value in pokemon.stats.items():
            stat_ratings[stat] = self.stats_stats['stats'][stat]['values'].index(value)/len(self.stats_stats['stats'][stat]['values'])
            print("Pokemon {} is at the top {}% of {}".format(pokemon_key, round(stat_ratings[stat]*100,2), stat))
        print(TypeAnalyzer.analyze(pokemon.types))

    def _computeStatTotals(self):
        for pokemon in self.pokemon:
            if pokemon.fully_evolved:
                for stat, value in pokemon.stats.items():
                    self.stats_stats['stats'][stat]['total'] += value
                    self.stats_stats['stats'][stat]['values'].append(value)
                    self.stats_stats['count'] += 1
                for form, value in pokemon.forms.items():
                    for s, v in value.stats.items():
                        self.stats_stats['stats'][s]['total'] += v
                        self.stats_stats['stats'][s]['values'].append(v)
                        self.stats_stats['count'] += 1
        for stat, value in self.stats_stats['stats'].items():
            self.stats_stats['stats'][stat]['values'].sort()

    def _computeStatAverages(self):
        for stat, value in self.stats_stats['stats'].items():
            self.stats_stats['stats'][stat]['average'] = value['total'] / self.stats_stats['count']

    @staticmethod
    def savePokedex(data, filename):
        with open(filename, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def loadPokedex(filename):
        with open(filename, 'rb') as handle:
            data = pickle.load(handle)
            return data
