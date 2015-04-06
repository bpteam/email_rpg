__author__ = 'iEC'

from abc import ABCMeta, abstractmethod


class Spell(object):
    __metaclass__ = ABCMeta
    manna_cost = 1

    @abstractmethod
    def cast(self, caster, target=False):
        pass