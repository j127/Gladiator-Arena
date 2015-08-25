"""Classes and functions to represents gladiators."""

from random import randint


class Gladiator(object):
    """Represents a gladiator."""

    def __init__(self, name, gladiator_class='fighter', gladiator_species='human'):
        self.name = name
        self.gladiator_class = gladiatorClass(gladiator_class)
        self.gladiator_species = gladiatorSpecies(gladiator_species)
        self.gold_coins = randint(2, 10) # should this be determined by gladiatorClass?

    def attack(self, target):
        return '{0} is attacking {1}'.format(self.name, target)

    def saving_throw(self, type):
        pass


    # Gold coins
    # Inventory: weapons, armor
    # Hit points
    # Armor class
    # Damage modifiers
    # gladiator class
    # gladiator species


class GladiatorClass(object):
    """Represents a gladiator class."""

    def __init__(self, gladiator_class):
        self.gladiator_class = gladiator_class

    def __repr__(self):
        return self.gladiator_class


class GladiatorSpecies(object):
    """Represents a gladiator species."""

    def __init__(self, gladiator_species):
        self.gladiator_species = gladiator_species

    def __repr__(self):
        return self.gladiator_species

