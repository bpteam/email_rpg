__author__ = 'iEC'

import src.Spells.Spell as Spell


class Illusion(Spell):
    manna_cost = 1

    def cast(self, caster):
        caster.manna -= self.manna_cost
        return True