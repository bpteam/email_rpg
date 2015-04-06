__author__ = 'iEC'

import src.Inventory.Bag as Bag
from abc import ABCMeta, abstractproperty
from random import randint


class Personage(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass
    max_health = 1
    health = 1
    skill = 1
    skill_effect = 0  # skills buff or debuff
    manna = 99
    bag = Bag

    def __init__(self, **attributes):
        for name in attributes.keys():
            self.__setattr__(self, name, attributes.get(name))

    def get_attack(self):
        return self.skill + randint(2, 12) + self.skill_effect

    def add_damage(self, damage):
        self.health -= damage

    def add_health(self, health):
        if (self.health + health) > self.max_health:
            self.health = self.max_health
        else:
            self.health += health

    def is_dead(self):
        return self.health <= 0