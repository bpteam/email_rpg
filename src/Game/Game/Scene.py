__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractmethod
from Game.Inventory.Loot import Loot


class Scene(metaclass=ABCMeta):
    number = 1
    commands = {"to the left": 425, "to the right": 14, "forward": 15}
    loot = Loot
    NPC = []
    default_commands = {
        'help': 'show_help',
        'drink water': 'drink_water',
        'put .+': 'put_item',
        'drop .+': 'drop_item'
    }

    def __init__(self, previous, command=False):
        pass

    @abstractmethod
    def run(self):
        pass