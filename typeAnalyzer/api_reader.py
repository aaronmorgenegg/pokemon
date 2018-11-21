import requests

from typeAnalyzer.constants import VERBOSITY, POKE_API


class API_Reader:
    def get(self, datatype, identifier):
        if VERBOSITY >= 2:
            print("Reading data from {}".format(POKE_API.format(datatype,identifier)))
        contents = requests.get(url=POKE_API.format(datatype, identifier))
        data = contents.json()
        return data
        
