__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Spells.Spell import Spell


class Copy(Spell):
    manna_cost = 1

    def cast(self, caster, target):
        """
        :param caster (Wizard):
        :param target (Wizard):
        :return:
        """
        caster.manna -= self.manna_cost
        enemy_copy = Copy
        enemy_copy.health = target.health
        enemy_copy.skill = target.skill
        return enemy_copy