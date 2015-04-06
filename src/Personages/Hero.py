__author__ = 'iEC'

import src.Personages.Personage as Personage


class Hero(Personage):
    manna = 10
    name = 'Hero'

    def cast_spell(self, spell, target=False):
        if self.has_manna_to_spell(spell):
            return spell.cast(self, target)
        else:
            return False

    def has_manna_to_spell(self, spell):
        return self.manna >= spell.manna_cost