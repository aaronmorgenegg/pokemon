
class Pokemon:
    def __init__(self, data):
        self.name = data['name']
        self.identifier = data['identifier']
        self.types = data['types']
        self.stats = data['stats']
        self.fully_evolved = data['fully_evolved']
        try:
            self.forms = data['forms']
        except KeyError:
            self.forms = None

