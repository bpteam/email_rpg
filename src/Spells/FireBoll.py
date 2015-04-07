__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Spells.Spell import Spell


class FireBoll(Spell):
    manna_cost = 1

    def cast(self, caster):
        caster.manna -= self.manna_cost
        return True