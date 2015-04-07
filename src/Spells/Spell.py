__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from abc import ABCMeta, abstractmethod


class Spell(object):
    __metaclass__ = ABCMeta
    manna_cost = 1

    @abstractmethod
    def cast(self, caster, target):
        pass