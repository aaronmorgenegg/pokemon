import requests
from constants import POKE_API, VERBOSITY

class API_Reader:
    def get(self, datatype, identifier):
        if VERBOSITY >= 2:
            print("Reading data from {}".format(POKE_API.format(datatype,identifier)))
        contents = requests.get(url=POKE_API.format(datatype, identifier))
        data = contents.json()
        return data
        
