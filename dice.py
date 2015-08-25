import re
from random import randint


class Die():
    """Represents a die."""

    def _roll_command_slicer(roll_command):
        """Processes a roll_command like '3d6' or '1d4+1'.
        
        It expects either two or three matches:
        1: the number of times the die should be rolled
        2: the number of sides on the dice
        3. the +/- modifier, which is optional

        Returns a tuple.
        """
        pattern = re.compile('(\d{1,4})d(\d{1,4})(\+\d{1,5})?')
        matches = re.match(pattern, roll_command).groups()
        matches_length = len(matches)

        if matches_length < 4 and matches_length > 1:
            return matches


    def _roller(roll_command_tuple):
        """Takes in a tuple, like ('2', '6', 'None') and rolls the dice.
        
        ('2', '6', 'None') means '2d6' without a +/- roll modifier.
        """
        pass


    def __init__(self, roll_command):
        # TODO: write this.
        self.num_sides = num_sides


    def __repr__(self):
        # TODO: rewrite this.
        return 'A {num}-sided die.'.format(num=self.num_sides)


    def roll(self, num_rolls=1, show_rolls=False):
        """Rolls a die a specified number of times. Defaults to one roll.
        Returns the sum of the rolls (integer), unless `show_rolls=True` in
        which case it returns a two-item list. The first item is the (integer)
        sum of the rolls. The second item is a list of the rolls.
        """
        # TODO: rewrite all of this.
        rolls = [randint(1, self.num_sides) for roll in range(num_rolls)]
        total = sum(rolls)
        if show_rolls is True:
            return [total, rolls]
        return total

