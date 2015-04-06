__author__ = 'iEC'

import src.Spells.Spell as Spell


class Power(Spell):
    manna_cost = 1

    def cast(self, caster):
        caster.manna -= self.manna_cost
        caster.skill_effect += 2
        return True