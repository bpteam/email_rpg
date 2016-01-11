__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractmethod
from src.Game.Inventory.Loot import Loot
import re


class Scene(metaclass=ABCMeta):
    number = 1
    need_save = False
    commands = {"to the left": 425, "to the right": 14, "forward": 15}
    loot = Loot()
    NPC = []
    command = False
    hero = None

    def __init__(self, command=False):
        self.command = command

    @abstractmethod
    def run(self):
        pass

    def exec(self, command):
        for name_command, method in self.commands:
            regexp = re.compile(name_command)
            match = regexp.search(command)
            if bool(match.group()):
                if bool(match.group('arg')):
                    eval('self.{0}'.format(method))(match.group('arg'))
                else:
                    eval('self.{0}'.format(method))()
                return True
        return False

    def command_exist(self, command):
        for name_command, method in self.commands:
            regexp = re.compile(name_command)
            match = regexp.search(command)
            if bool(match.group()):
                return True
        return False

    def get_command_action(self, command):
        for name_command, method in self.commands:
            regexp = re.compile(name_command)
            match = regexp.search(command)
            if bool(match.group()):
                return match.group()
        return False

    def command_executable(self, command):
        action = self.get_command_action(command)
        if bool(action):
            return isinstance(action, str)
        return False