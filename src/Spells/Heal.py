__author__ = 'iEC'

import src.Spells.Spell as Spell


class Heal(Spell):
    manna_cost = 1

    def cast(self, caster):
        caster.manna -= self.manna_cost
        caster.add_health(8)
        return True