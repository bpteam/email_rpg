__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Spells.Spell import Spell
from src.Personages.PersonageCopy import PersonageCopy


class Copy(Spell):
    manna_cost = 1

    def cast(self, caster, target):
        """
        :param caster (Wizard):
        :param target (Wizard):
        :return:
        """
        caster.manna -= self.manna_cost
        return PersonageCopy({'health': target.health, 'skill': target.skill})