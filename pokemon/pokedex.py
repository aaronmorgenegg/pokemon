import pickle


class Pokedex:
    """Contains a list of pokemon, and operations on those pokemon"""
    def __init__(self, data):
        self.pokemon = data['pokemon']

    def tallyTypes(self):
        try:
            return self.tallied_types
        except AttributeError:
            self.tallied_types = {}

            for pokemon in self.pokemon:
                types = pokemon.types
                for t in types:
                    try:
                        self.tallied_types[t] += 1
                    except KeyError:
                        self.tallied_types[t] = 1
                for form, value in pokemon.forms.items():
                    if form != 'partner':
                        for t in value.types:
                            try:
                                self.tallied_types[t] += 1
                            except KeyError:
                                self.tallied_types[t] = 1

            return self.tallied_types

    def computeStatsStats(self):
        """Compute various statistics(average, std dev) about pokemon stats(hp, attack etc)"""
        try:
            return self.stats_stats
        except AttributeError:
            self.stats_stats = {}

            for pokemon in self.pokemon:
                types = pokemon.types
                for t in types:
                    try:
                        self.stats_stats[t] += 1
                    except KeyError:
                        self.stats_stats[t] = 1
                for form, value in pokemon.forms.items():
                    if form != 'partner':
                        for t in value.types:
                            try:
                                self.stats_stats[t] += 1
                            except KeyError:
                                self.stats_stats[t] = 1

            return self.stats_stats

    @staticmethod
    def savePokedex(data, filename):
        with open(filename, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def loadPokedex(filename):
        with open(filename, 'rb') as handle:
            data = pickle.load(handle)
            return data
