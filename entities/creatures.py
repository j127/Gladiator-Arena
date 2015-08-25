"""Classes and functions to represents characters."""

from random import randint


class Creature(object):
    """Represents a character."""

    def __init__(self, name, character_class='fighter', character_species='human'):
        self.name = name
        self.character_class = CharacterClass(character_class)
        self.character_species = CharacterSpecies(character_species)
        self.gold_coins = randint(2, 10) # should this be determined by CharacterClass?

    def attack(self, target):
        return '{0} is attacking {1}'.format(self.name, target)

    def saving_throw(self, type):
        pass


    # Gold coins
    # Inventory: weapons, armor
    # Hit points
    # Armor class
    # Damage modifiers
    # Character class
    # Character species


class CharacterClass(object):
    """Represents a character class."""

    def __init__(self, character_class):
        self.character_class = character_class

    def __repr__(self):
        return self.character_class


class CharacterSpecies(object):
    """Represents a character species."""

    def __init__(self, character_species):
        self.character_species = character_species

    def __repr__(self):
        return self.character_species

