__author__ = 'iEC'

import src.Spells.Spell as Spell
import copy


class Copy(Spell):
    manna_cost = 1

    def cast(self, caster, target):
        caster.manna -= self.manna_cost
        return copy.copy(target)