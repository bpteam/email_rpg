__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractmethod


class Spell(metaclass=ABCMeta):
    manna_cost = 1

    @abstractmethod
    def cast(self, caster, target):
        pass