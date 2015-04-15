__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from random import randint


class Dice(object):
    dice_min = 1
    dice_max = 6

    @staticmethod
    def throw(count=1):
        return randint(Dice.dice_min * count, Dice.dice_max * count)