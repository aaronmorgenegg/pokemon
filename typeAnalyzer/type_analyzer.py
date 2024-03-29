from typeAnalyzer.api_reader import API_Reader
from typeAnalyzer.constants import TYPES


class TypeAnalyzer:
    type_cache = {}
    @staticmethod
    def analyze(types):
        if len(types) == 1:
            return TypeAnalyzer.analyzeSingleType(types[0])
        elif len(types) == 2:
            return TypeAnalyzer.analyzeDoubleType(types)
        else:
            raise Exception('Invalid # of types to be analyzed')

    @staticmethod
    def analyzeSingleType(single_type):
        try:
            return TypeAnalyzer.type_cache[single_type]
        except KeyError:
            type_data = {'defense': {}, 'attack': {}}
            for t in TYPES:
                type_data['defense'][t] = 1.0
                type_data['attack'][t] = 1.0
            api = API_Reader()
            response = api.get("type", single_type)
            TypeAnalyzer.extractDamageRelations(response, type_data)

            TypeAnalyzer.type_cache[single_type] = type_data
            return type_data

    @staticmethod
    def extractDamageRelations(response, type_data):
        damage_relations = response['damage_relations']
        for relation in damage_relations['no_damage_to']:
            type_data['attack'][relation['name']] = 0.0
        for relation in damage_relations['half_damage_to']:
            type_data['attack'][relation['name']] = .5
        for relation in damage_relations['double_damage_to']:
            type_data['attack'][relation['name']] = 2.0
        for relation in damage_relations['no_damage_from']:
            type_data['defense'][relation['name']] = 0.0
        for relation in damage_relations['half_damage_from']:
            type_data['defense'][relation['name']] = .5
        for relation in damage_relations['double_damage_from']:
            type_data['defense'][relation['name']] = 2.0

    @staticmethod
    def analyzeDoubleType(types):
        dual_type = types[0] + "-" + types[1]
        try:
            return TypeAnalyzer.type_cache[dual_type]
        except KeyError:
            type_data = {'defense': {}, 'attack': {}}
            type_data1 = TypeAnalyzer.analyzeSingleType(types[0])
            type_data2 = TypeAnalyzer.analyzeSingleType(types[1])

            for key, value in type_data1['attack'].items():
                type_data['attack'][key] = value * type_data2['attack'][key]
            for key, value in type_data1['defense'].items():
                type_data['defense'][key] = value * type_data2['defense'][key]

            TypeAnalyzer.type_cache[dual_type] = type_data
            return type_data
