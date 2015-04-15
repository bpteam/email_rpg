__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Game.Spells import Spell
from DungeonOfBlackCastle.Personages import PersonageCopy


class Copy(Spell):
    manna_cost = 1

    def cast(self, caster, target):
        """
        :param caster (Wizard):
        :param target (Personage):
        :return (PersonageCopy):
        """
        caster.manna -= self.manna_cost
        return PersonageCopy({'health': target.health, 'skill': target.skill})