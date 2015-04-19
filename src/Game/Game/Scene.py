__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractmethod
from Game.Inventory.Loot import Loot
from Game.Game.MessageText import MessageText


class Scene(metaclass=ABCMeta):
    number = 1
    need_save = False
    commands = {"to the left": 425, "to the right": 14, "forward": 15}
    loot = Loot()
    NPC = []
    command = False

    def __init__(self, command=False):
        self.command = command

    @abstractmethod
    def run(self):
        pass