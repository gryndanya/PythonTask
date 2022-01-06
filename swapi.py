import pandas as pd
import sw_utils as utl
from collections import defaultdict


class Crew:
    """Represents a Starship or Vehicle crew.

    Attributes:
        Accepts a dictionary of Person and/or Droid crew members and assigns each key-value pair
        to the new `Crew` instance's `__dict__` dictionary of writable attributes.

        < role > (Person | Droid): Person or Droid instance identified by crew role (e.g., pilot)

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, crew_members):
        """Initialize Crew instance. Loops over the passed in dictionary and calls the built-in
        function < setattr() > to create each instance variable and assign the value. The
        dictionary key (e.g., "pilot") serves as the instance variable name to which the
        accompanying < Person | Droid > instance is assigned as the value, e.g.,
        {< role >: < Person | Droid >, ...}

        Parameters:
            crew_members (dict): crew members dictionary

        Returns:
            None
        """

        for key, val in crew_members.items():
            setattr(self, key, val)  # call built-in function

    def __str__(self):
        """Loops over the instance variables and return a string representation of each crew
        member < Person | Droid > object per the following format:

        < position >: < crew member name > e.g., "pilot: Han Solo, copilot: Chewbacca"
        """

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}"  # additional member
            else:
                crew = f"{key}: {val}"  # 1st member

        return crew

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over a < Crew > instance's
        __dict__ items and assigns new key-value pairs to an empty dictionary using the existing
        key as the new key and a dictionary representation of the < Person > or < Droid > instance
        as the value. After the loop terminates the new dictionary is returned to the caller.
        Do not simply return self.__dict__. It can be intercepted and mutated, adding, modifying
        and/or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable()  # person or droid object

        return crew


class Droid:
    """Represents a mechanical being that possesses artificial intelligence.

    Attributes:
       Required
            url (str): identifier/locator (required)
            name (str): droid name (required)
            model (str): droid model (required)
        Optional
            manufacturer (str): creator
            create_year (str): year of manufacture
            height_m (float): height in meters
            mass_kg (float): mass in kilograms
            equipment (list): equipment carried, if any

    Methods:
        jsonable: return JSON-friendly dict representation of the object
        store_instructions: provides Droid instance with data to store
    """

    def __init__(self, url, name, model):
        """Initialize a Droid instance."""
        self.url = url
        self.name = name
        self.model = model

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            model
            manufacturer
            create_year
            height_m
            mass_kg
            equipment
        """
        result = {}
        keys = ['url', 'name', 'model', 'manufacturer', 'create_year', 'height_m', 'mass_kg', 'equipment']
        for key in keys:
            result[key] = getattr(self, key)

        return result


class Passengers:
    """Represents passengers carried on a Starship or Vehicle.

    Attributes:
        Accepts a list of < Person > and/or < Droid > objects that are added as key-value pairs
        to the new Passengers instance's `__dict__` dictionary of writable attributes. The
        < Person > or < Droid > "name" value serves as the key and the instance itself as the
        value. Each key-value pair added to __dict__ represents a new instance variable and value.

        < "name" > (Person | Droid): Person or Droid instance identified by name

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, passengers):
        """Initialize Passengers instance. Loops over the passed in list of < Person > and/or
        < Droid > instances and calls the built-in function < setattr() > to create the instance
        variable and assign the value. The < Droid > or < Person > instance's "name" value serves
        as the new instance variable name (see format below) while the < Person > or < Droid >
        instance is assigned as the value.

        Instance variable name formatting rules:
            1. Change name to lowercase
            2. Replace space (' ') with underscore ('_')
            3. Replace dash ('-') with underscore ('_')

            "Luke Skywalker" -> "luke_skywalker"
            self.luke_skywalker = < Person >

            "C-3PO" -> "c_3po"
            self.c_3po = < Droid >

        Parameters:
            passengers (list): list of < Person > and/or < Droid > objects

        Returns:
            None
        """

        pass  # TODO Implement

    def __str__(self):
        """Loops over instance variable values and returns a string representation of each
        passenger < Person > or < Droid > object (passenger name only)."""

        passengers = None
        for val in self.__dict__.values():
            if passengers:
                passengers = f"{passengers}, {val.name}"  # additional member
            else:
                passengers = f"Passengers: {val.name}"  # 1st passenger

        return passengers

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over the < Passengers >
        instance's __dict__ values and converts each < Person > or < Droid > object encountered
        to a dictionary. Accumulates dictionaries in a < list >.  After the loop terminates the
        new list is returned to the caller. Do not simply return self.__dict__. It can be
        intercepted and mutated, adding, modifying and/or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            list: nested person or droid dictionaries
        """

        pass  # TODO Implement


class Person:
    """Represents a person.

    Attributes:
        url (str): identifer/locator
        name (str): person name
        birth_year (str): person's birth_year
        height_m (float): person's height in centimeters
        mass_kg (float): person's weight in kilograms
        homeworld (Planet): person's home planet
        force_sensitive (bool): ability to harness the power of the Force.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, force_sensitive=False):
        """Initialize a Person instance."""
        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.force_sensitive = force_sensitive

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes
        as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
           url
           name
           birth_year
           height_m
           mass_kg
           homeworld
           force_sensitive
        """
        result = {}
        keys = ['url', 'name', 'birth_year', 'height_m', 'mass_kg', 'homeworld', 'force_sensitive']
        for key in keys:
            result[key] = getattr(self, key)

        return result


class Planet:
    """Represents a planet.

    Attributes:
        url (str): identifier/locator
        name (str): planet name
        region (str): region name
        sector (str): sector name
        suns (int): number of suns
        moons (int): number of moons
        orbital_period_days (float): orbital period around sun(s) measured in
                                     standard days
        diameter_km (int): diameter of planet measured in kilometers
        gravity_std (dict): gravity level
        climate (list): climate type(s) found on planet
        terrain (list): terrain type(s) found on planet
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):
        self.url = url
        self.name = name

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes
        as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            region
            sector
            suns
            moons
            orbital_period_days
            diameter_km
            gravity_std
            climate
            terrain
            population
        """
        result = {}
        keys = ['url', 'name', 'region', 'sector', 'suns', 'moons', 'orbital_period_days', 'diameter_km', 'gravity_std',
                'climate', 'terrain', 'population']
        for key in keys:
            result[key] = getattr(self, key)

        return result


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        manufacturer (str): starship builder
        length_m (float): starship length in meters
        max_atmosphering_speed (int): maximum sub-orbital speed
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament [list]: offensive and defensive weaponry
        crew_members (Crew): Crew instance assigned to starship
        passengers_on_board (Passengers): passengers on board starship
        cargo_capacity_kg (float): cargo capacity in kilograms that the starship rated to carry
        consumables (str): max period in months before on-board provisions must be replenished

    Methods:
        assign_crew_members: assign < Crew > instance to starship
        add_passengers: assign < Passengers > instance to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class):
        """Initalize instance of a Starship."""
        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.MGLT = None
        self.crew_members = None
        self.passengers_on_board = None

    def __str__(self):
        """String representation of the object."""

        return self.model  # not name (which is usually too generic)

    def add_passengers(self, passengers):
        """Assigns passengers to the instance variable < self.passengers_on_board > if passenger
        accommodations on the starship are available. Confirms that the passed in < passengers >
        argument is an instance of the < Passengers > class. If not a < Passengers > instance the
        < self.passengers_on_board > variable assignment is NOT performed.

        Parameters:
            passengers (Passengers): object containing < Person | Droid > instances

        Returns:
            None
        """
        self.passengers_on_board = passengers

    def assign_crew_members(self, crew):
        """Assigns crew members to the instance variable < self.crew_members > if the crew size
        can be accommodated. Confirms that the passed in < crew > argument is an instance of
        the < Crew > class. If not a < Crew > instance the < self.crew_members > variable assignment
        is NOT performed.

        Parameters:
            crew (Crew): object comprising crew members ('< role >': < Person> / < Droid >)

        Returns:
            None
        """
        self.crew_members = crew

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            model
            starship_class
            manufacturer
            length_m
            max_atmosphering_speed
            hyperdrive_rating
            MGLT
            armament
            crew_members
            passengers_on_board
            cargo_capacity_kg
            consumables
        """

        result = {}
        keys = ['url', 'name', 'model', 'starship_class', 'manufacturer', 'length_m',
                'max_atmosphering_speed', 'hyperdrive_rating', 'MGLT', 'armament', 'crew_members',
                'passengers_on_board', 'cargo_capacity_kg', 'consumables']
        for key in keys:
            result[key] = getattr(self, key)

        return result


def convert_episode_values(episodes):
    """Converts select string values to either int, float, list, or None in the passed in list of
    nested dictionaries. The function delegates to the `convert_to_*` functions located in the
    module `swapi_utils` the task of converting the specified strings to either int, float, or
    list. Converting empty or blank values to None is handled locally.

    Conversions:
        str to None: all blank or empty values
        str to int: 'series_season_num', 'series_episode_num', 'season_episode_num'
        str to float: 'episode_prod_code', 'episode_us_viewers_mm'
        str to list: 'episode_writers'

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: nested episode dictionaries containing mutated key-value pairs
    """
    for ep in range(len(episodes)):
        for key in episodes[ep]:
            episodes[ep][key] = utl.convert_to_none(episodes[ep][key])
            if episodes[ep][key] == '':
                episodes[ep][key] = None
            else:
                if key == 'series_season_num' or key == 'series_episode_num' or key == 'season_episode_num':
                    episodes[ep][key] = utl.convert_to_int(episodes[ep][key])
                if key == 'episode_prod_code' or key == 'episode_us_viewers_mm':
                    episodes[ep][key] = utl.convert_to_float(episodes[ep][key])
                if key == 'episode_writers':
                    episodes[ep][key] = utl.convert_to_list(episodes[ep][key],', ')
    return episodes


def count_episodes_by_director(episodes):
    """Constructs and returns a dictionary of key-value pairs that associate each director with a
    count of the episodes that they directed. The director's name comprises the key and the
    associated value a count of the number of episodes they directed. Duplicate keys are NOT
    permitted.

    Format:
        {
            < director name >: < episode count >,
            < director name >: < episode count >,
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that store counts of the number of episodes directed
              by each director
    """
    result = {}
    for ep in range(len(episodes)):
        if episodes[ep]['episode_director'] in result:
            result[episodes[ep]['episode_director']] += 1
        else:
            result[episodes[ep]['episode_director']] = 1
    return result


def create_droid(data):
    """Creates a < Droid > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible. Adding special instructions constitutes a seperate
    operation.

    Type conversions:
        height -> height_m (str to float)
        mass -> mass_kg (str to float)
        equipment -> equipment (str to list)

    Parameters:
        data (dict): source data

    Returns:
        Droid: new < Droid > instance
    """
    keys = ['url', 'name', 'model', 'manufacturer', 'create_year', 'height', 'mass', 'equipment']

    for key in keys:
        data[key] = utl.convert_to_none(data[key])
        if data[key] is not None:
            if key == 'height' or key == 'mass':
                data[key] = utl.convert_to_float(data[key])
            if key == 'equipment':
                data[key] = utl.convert_to_list(data[key], '|')

    droid = Droid(data['url'], data['name'], data['model'])

    for key in keys:
        if key == 'height':
            setattr(droid, 'height_m', utl.convert_to_float(data[key]))
        elif key == 'mass':
            setattr(droid, 'mass_kg', data[key])
        else:
            setattr(droid, key, data[key])
    return droid


def create_person(data, planets=None):
    """Creates a < Person > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible. Calls < utl.get_swapi_resource() > to retrieve homeworld
    data. Adds additional planet information to the homeworld data dictionary if an optional
    < planets > dictionary is passed in as a second argument. Calls < create_planet() > to add
    a < Planet > object to the person instance before returning the new instance to the caller.

    Type conversions:
        height -> height_m (str to float)
        mass -> mass_kg (str to float)
        homeworld -> homeworld (str to Planet)

    Parameters:
        data (dict): source data
        planets (list): optional supplemental planetary data

    Returns:
        Person: new < Person > instance
    """
    keys = ['url', 'name', 'birth_year', 'height', 'mass', 'homeworld', 'force_sensitive']

    for key in keys:
        data[key] = utl.convert_to_none(data[key])
        if data[key] is not None:
            if key == 'height' or key == 'mass':
                data[key] = utl.convert_to_float(data[key])

    person = Person(data['url'], data['name'], data['birth_year'], data['force_sensitive'])

    for key in keys:
        if key == 'height':
            setattr(person, 'height_m', utl.convert_to_float(data[key]))
        elif key == 'mass':
            setattr(person, 'mass_kg', utl.convert_to_float(data[key]))
        elif key == 'homeworld':
            tatooine_data = utl.get_swapi_resource(data[key])
            for key in planets[12]:
                tatooine_data[key] = planets[12][key]
            tatooine = create_planet(tatooine_data)
            setattr(person, 'homeworld', tatooine.jsonable())
        else:
            setattr(person, key, data[key])
    return person


def create_planet(data):
    """Creates a < Planet > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible.

    Type conversions:
        suns -> suns (str->int)
        moon -> moons (str->int)
        orbital_period_days -> orbital_period_days (str to float)
        diameter -> diameter_km (str to int)
        gravity -> gravity_std (str to float)
        climate -> climate (str to list)
        terrain -> terrain (str to list)
        population -> population (str->int)

    Parameters:
        data (dict): source data

    Returns:
        Planet: new < Planet > instance
    """
    keys = ['url', 'name', 'region', 'sector', 'suns', 'moons', 'orbital_period', 'diameter', 'gravity',
            'climate', 'terrain', 'population']
    for key in keys:
        data[key] = utl.convert_to_none(data[key])
        if data[key] is not None:
            if key == 'suns' or key == 'moons' or key == 'diameter' or key == 'population':
                data[key] = utl.convert_to_int(data[key])
            if key == 'climate' or key == 'terrain':
                data[key] = utl.convert_to_list(data[key], ', ')
            if key == 'orbital_period_days':
                data[key] = utl.convert_to_float(data[key])
            if key == 'gravity':
                data[key] = utl.convert_gravity_value(data[key])
    planet = Planet(data['url'], data['name'])
    for key in keys:
        if key == 'orbital_period':
            setattr(planet, 'orbital_period_days', utl.convert_to_float(data[key]))
        elif key == 'diameter':
            setattr(planet, 'diameter_km', data[key])
        elif key == 'gravity':
            setattr(planet, 'gravity_std', data[key])
        else:
            setattr(planet, key, data[key])
    return planet


def create_starship(data):
    """Creates a < Starship > instance from dictionary data, converting optional string values to
    the appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to float)

    Parameters:
        data (dict): source data

    Returns:
        starship: a new < Starship > instance
    """
    keys = ['url', 'name', 'model', 'starship_class', 'manufacturer', 'length', 'max_atmosphering_speed',
            'hyperdrive_rating',
            'MGLT', 'armament', 'crew', 'passengers', 'cargo_capacity', 'consumables']
    for key in keys:
        data[key] = utl.convert_to_none(data[key])
        if data[key] is not None:
            if key == "max_atmosphering_speed" or key == "cargo_capacity":
                data[key] = int(data[key])
            if key == 'armament':
                data[key] = utl.convert_to_list(data[key], ',')
            if key == 'length_m' or 'hyperdrive_rating':
                data[key] = utl.convert_to_float(data[key])

    starship = Starship(data['url'], data['name'], data['model'], data['starship_class'])
    for key in keys:
        if key == 'length':
            setattr(starship, 'length_m', data[key])
        elif key == 'MGLT':
            setattr(starship, 'MGLT', None)
        elif key == 'crew':
            setattr(starship, 'crew_members', None)
        elif key == 'passengers':
            setattr(starship, 'passengers_on_board', None)
        elif key == 'cargo_capacity':
            setattr(starship, 'cargo_capacity_kg', int(data[key]))
        elif key == 'max_atmosphering_speed':
            setattr(starship, 'max_atmosphering_speed', int(data[key]))
        else:
            setattr(starship, key, data[key])
    return starship


def get_least_viewed_episode(episodes):
    """Identifies and returns episode with the lowest recorded viewership. Ignores episodes with
    no viewship value. Ignores ties. Delegates to the function < has_viewer_data > the task of
    determing if the episode includes viewership "episode_us_viewers_mm" data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: episode with the lowest recorded viewership.
    """
    maxi = episodes[0]['episode_us_viewers_mm']
    index = 0
    for ep in range(len(episodes)):
        if has_viewer_data(episodes[ep]):
            if utl.convert_to_float(episodes[ep]['episode_us_viewers_mm']) < maxi:
                maxi = episodes[ep]['episode_us_viewers_mm']
                index = ep
    return episodes[index]


def get_most_viewed_episode(episodes):
    """Identifies and returns the episode with the highest recorded viewership. Ignores episodes
    with no viewship value. Ignores ties. Delegates to the function < has_viewer_data > the task
    of determing if the episode includes viewership "episode_us_viewers_mm" data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: episode with the highest recorded viewership.
    """
    maxi = episodes[0]['episode_us_viewers_mm']
    index = 0
    for ep in range(len(episodes)):
        if has_viewer_data(episodes[ep]):
            if utl.convert_to_float(episodes[ep]['episode_us_viewers_mm']) > maxi:
                maxi = episodes[ep]['episode_us_viewers_mm']
                index = ep
    return episodes[index]


def group_episodes_by_writer(episodes):
    """Utilizes a dictionary to group individual episodes by a contributing writer. The writer's
    name comprises the key and the associated value comprises a list of one or more episode
    dictionaries. Duplicate keys are NOT permitted.

    Format:
        {
            < writer name >: [{< episode_01 >}, {< episode_02 >}, ...],
            < writer name >: [{< episode_01 >}, {< episode_02 >}, ...],
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that groups episodes by a contributing writer
    """
    result = {}
    for ep in range(len(episodes)):
        print(episodes[ep]['episode_writers'])
        for write in episodes[ep]['episode_writers']:
            if write in result:
                result[write] += [(episodes[ep])]
            else:
                result[write] = [(episodes[ep])]

    return result


def has_viewer_data(episode):
    """Checks the truth value of an episode's "episode_us_viewers_mm" key-value pair. Returns
    True if the truth value is "truthy" (e.g., numeric values that are not 0, non-empty sequences
    or dictionaries, boolean True); otherwise returns False if a "falsy" value is detected (e.g.,
    empty sequences (including empty or blank strings), 0, 0.0, None, boolean False)).

    Parameters:
        episode (dict): represents an episode

    Returns:
        bool: True if "episode_us_viewers_mm" value is truthy; otherwise False
    """
    return isinstance(utl.convert_to_float(episode['episode_us_viewers_mm']), float)


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    # 8.1 CHALLENGE 01
    # 8.1.1
    clone_wars = utl.read_csv("clone_wars.csv")
    clone_wars.pop(0)

    # 8.1.2.1
    clone_wars_22 = clone_wars[0:4]
    # 8.1.2.2
    clone_wars_2012 = clone_wars[3:5]
    # 8.1.2.3
    clone_wars_url = clone_wars[5]

    # 8.1.2.4
    clone_wars_even_num_seasons = [clone_wars[0], clone_wars[1], clone_wars[2], clone_wars[3], clone_wars[4],
                                   clone_wars[6]]

    # 8.2 CHALLENGE 02
    # 8.2.1
    clone_wars_episodes = utl.read_csv_to_dicts('clone_wars_episodes.csv')
    utl.write_json('test.json', clone_wars_episodes)
    check = 0
    for episode in clone_wars_episodes:
        if has_viewer_data(episode):
            check += 1

    # 8.3 Challenge 03
    # print(f"\nconvert_to_int converted = {utl.convert_to_list('506')}")
    # print(f"\nconvert_to_int no change = {utl.convert_to_list('unknown')}")
    # print(f"\nconvert_to_int no change = {utl.convert_to_list([506, 507])}")
    # print(f"\nconvert_to_int converted = {utl.convert_to_float('506')}")
    # print(f"\nconvert_to_int no change = {utl.convert_to_float('unknown')}")
    # print(f"\nconvert_to_int no change = {utl.convert_to_float([506, 507])}")
    # print(f"\nconvert_to_int converted = {utl.convert_to_int('506')}")
    # print(f"\nconvert_to_int no change = {utl.convert_to_int('unknown')}")
    # print(f"\nconvert_to_int no change = {utl.convert_to_int([506, 507])}")

    # 8.4 Challenge 04
    clone_wars_episodes = convert_episode_values(clone_wars_episodes)
    utl.write_json('stu-clone_wars-episodes_converted.json', clone_wars_episodes)
    # 8.5 Challenge 05
    most_viewed_episode = get_most_viewed_episode(clone_wars_episodes)
    least_viewed_episode = get_least_viewed_episode(clone_wars_episodes)

    # 8.6 Challenge 06
    director_episode_counts = count_episodes_by_director(clone_wars_episodes)
    utl.write_json('stu-clone_wars-director_episode_counts.json', director_episode_counts)

    # 8.7 CHALLENGE 07
    writer_episodes = group_episodes_by_writer(clone_wars_episodes)
    utl.write_json('stu-clone_wars-writer_episodes.json', writer_episodes)
    # 8.8 CHALLENGE 08
    # returns None (converted)
    # returns 'Yoda' (no change)
    # returns [1, 2, 3] (no change, exception caught)
    # print(f"\nChallenge 08: convert_to_none('Unknown') = {utl.convert_to_none('Unknown')}")
    # print(f"\nChallenge 08: convert_to_none('Yoda') = {utl.convert_to_none('Yoda')}")
    # print(f"\nChallenge 08: convert_to_none([1, 2, 3]) = {utl.convert_to_none([1, 2, 3])}")
    # returns 1.0 (converted)
    # returns 1.56 (converted)
    # returns [1, 2, 3] (no change; exception caught)
    # print(f"\nChallenge 08: convert_gravity_value('1 standard') = {utl.convert_gravity_value('1 standard')}")
    # print(f"\nChallenge 08: convert_gravity_value('1.56') = {utl.convert_gravity_value('1.56')}")
    # print(f"\nChallenge 08: convert_gravity_value([1, 2, 3]) = {utl.convert_gravity_value([1, 2, 3])}")

    # 8.9 CHALLENGE 09
    wookiee_planets = utl.read_csv_to_dicts('wookieepedia_planets.csv')
    tatooine_data = utl.get_swapi_resource("https://swapi.py4e.com/api/planets/1")

    for key in wookiee_planets[12]:
        tatooine_data[key] = wookiee_planets[12][key]

    tatooine = create_planet(tatooine_data)
    utl.write_json('stu-tatooine.json', tatooine.jsonable())

    # 8.10 CHALLENGE 10
    wookiee_droids = utl.read_json('wookieepedia_droids.json')
    r2_d2_data = utl.get_swapi_resource("https://swapi.py4e.com/api/people/3")

    for key in wookiee_droids[2]:
        r2_d2_data[key] = wookiee_droids[2][key]

    r2_d2 = create_droid(r2_d2_data)
    utl.write_json('stu-r2_d2.json', r2_d2.jsonable())
    # 8.11 Challenge 11
    wookiee_people = utl.read_json('wookieepedia_people.json')
    anakin_data = utl.get_swapi_resource('https://swapi.py4e.com/api/people/1/')

    for key in wookiee_people[1]:
        if key != 'homeworld':
            anakin_data[key] = wookiee_people[1][key]

    anakin = create_person(anakin_data, wookiee_planets)
    utl.write_json('stu-anakin_skywalker.json', anakin.jsonable())

    # 8.12 CHALLENGE 12
    wookiee_starships = utl.read_csv_to_dicts('wookieepedia_starships.csv')
    twilight_data = wookiee_starships[5]
    twilight = create_starship(twilight_data)
    utl.write_json('stu-twilight.json', twilight.jsonable())
    # 8.13 CHALLENGE 13

    # 8.14 CHALLENGE 14


if __name__ == '__main__':
    main()
