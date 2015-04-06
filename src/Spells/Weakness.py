__author__ = 'iEC'

import src.Spells.Spell as Spell


class Weakness(Spell):
    manna_cost = 1

    def cast(self, caster, target):
        caster.manna -= self.manna_cost
        target.skill_effect += -2
        return True