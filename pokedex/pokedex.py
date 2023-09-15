import requests


class Pokedex(object):
    """
    The main class for interacting with the Pokédex API, and the starting
    point for any application using this library.
    """
    def __init__(self, **kwargs):
        """
        Pokédex constructor, creates an instance of the Pokédex class to get
        you started with the library.
        """
        super(Pokedex, self).__init__()

        self.BASE_URL = 'https://ex.traction.one/pokedex'
        self.USER_AGENT = kwargs.get('useragent', 'pokedex.py')
        self.AUTH = kwargs.get('authorization', None)
        self.headers = {
            'Accept': 'application/json',
            'Authorization': self.AUTH,
            'User-Agent': self.USER_AGENT,
        }

    def make_request(self, path):
        res = requests.get(path, headers=self.headers)
        if res.ok:
            return res.json()
        else:
            return res.raise_for_status()

    def get_evolution_stone(self, slug):
        """
        Returns the details of the specified evolution stone.
        """
        endpoint = '/evolution/stones/' + slug
        return self.make_request(self.BASE_URL + endpoint)

    def get_pokemon(self, name):
        """
        Returns the details of the specified Pokémon and its forms.
        """
        endpoint = '/pokemon/' + str(name)
        return self.make_request(self.BASE_URL + endpoint)

    def list_evolution_stones(self):
        """
        Returns a list of all the evolution stones.
        """
        endpoint = '/evolution/stones'
        return self.make_request(self.BASE_URL + endpoint)

    def list_pokemon(self, number):
        """
        Returns a list of all the discovered Pokémon.
        """
        endpoint = '/pokemon/'
        return self.make_request(self.BASE_URL + endpoint)
