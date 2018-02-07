import requests


class Pokedex(object):
    """
    The main class for interacting with the Pokedex API, and the starting
    point for any application using this library.
    """
    def __init__(self, **kwargs):
        """
        Pokedex constructor, creates an instance of the Pokedex class to get
        you started with the library.
        """
        super(Pokedex, self).__init__()

        base_url = 'https://pokeapi.bastionbot.org'

        version = kwargs.get('version', None)
        if (version):
            self.BASE_URL = base_url + '/' + version
        else:
            self.BASE_URL = base_url

        self.USER_AGENT = kwargs.get('user_agent', 'pokedex.py (https://github.com/PokeDevs/pokedex.py, v1.0.0)')
        self.AUTH = kwargs.get('auth', None)
        self.headers = {
            'User-Agent': self.USER_AGENT,
            'Accept': 'application/json',
            'Auth': self.AUTH
        }

    def make_request(self, path):
        res = requests.get(path, headers=self.headers)
        if res.ok or res.status_code == 404:
            return res.json()
        else:
            return res.raise_for_status()

    # Endpoint: /categories
    def get_categories(self):
        """
        Returns an array of Pokemon Categories discovered in the Pokemon
        World.
        """
        endpoint = '/categories'
        return self.make_request(self.BASE_URL + endpoint)

    # Endpoint: /egg-groups
    def get_egg_groups(self):
        """
        Returns an array of Pokemon Egg Groups discovered in the Pokemon
        World.
        """
        endpoint = '/egg-groups'
        return self.make_request(self.BASE_URL + endpoint)

    # Endpoint: /evolution-stone
    def get_evolution_stones(self):
        """
        Returns an array of Pokemon Evolution Stone names discovered in the
        Pokemon world.
        """
        endpoint = '/evolution-stone'
        return self.make_request(self.BASE_URL + endpoint)

    def get_evolution_stone(self, slug):
        """
        Returns a Evolution Stone object containing the details about the
        evolution stone.
        """
        endpoint = '/evolution-stone/' + slug
        return self.make_request(self.BASE_URL + endpoint)

    # Endpoint: /league
    def get_leagues(self):
        """
        Returns an array of Pokemon League names known to us.
        """
        endpoint = '/league'
        return self.make_request(self.BASE_URL + endpoint)

    def get_league(self, slug):
        """
        Returns a Pokemon League object containing the details about the
        league.
        """
        endpoint = '/league/' + slug
        return self.make_request(self.BASE_URL + endpoint)

    # Endpoint: /pokemon
    def get_pokemon_by_name(self, name):
        """
        Returns an array of Pokemon objects containing all the forms of the
        Pokemon specified the name of the Pokemon.
        """
        endpoint = '/pokemon/' + str(name)
        return self.make_request(self.BASE_URL + endpoint)

    def get_pokemon_by_number(self, number):
        """
        Returns an array of Pokemon objects containing all the forms of the
        Pokemon specified the Pokedex number.
        """
        endpoint = '/pokemon/' + str(number)
        return self.make_request(self.BASE_URL + endpoint)

    def get_pokemon(self, number):
        """
        Depricated: Use get_pokemon_by_number() instead.
        """
        return self.get_pokemon_by_number(number)

    def get_pokemon_counts(self):
        """
        Returns a Pokemon Counts object containing the number of Pokemon in
        each generation and the total number of Pokemon in the Pokemon World.
        """
        endpoint = '/pokemon/counts'
        return self.make_request(self.BASE_URL + endpoint)

    # Endpoint: /types
    def get_types(self):
        """
        Returns an array of Pokemon Types discovered in the Pokemon World.
        """
        endpoint = '/types'
        return self.make_request(self.BASE_URL + endpoint)
