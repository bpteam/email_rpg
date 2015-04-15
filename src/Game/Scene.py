__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractmethod


class Scene(metaclass=ABCMeta):
    current = 1
    commands = {"to the left": 425, "to the right": 14, "forward": 15}

    @abstractmethod
    def __init__(self, previous=1, command=False):
        pass

    @abstractmethod
    def load_commands(self):
        pass

    @abstractmethod
    def build(self):
        pass