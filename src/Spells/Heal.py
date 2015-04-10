__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Spells.Spell import Spell


class Heal(Spell):
    manna_cost = 1

    def cast(self, caster, target):
        caster.manna -= self.manna_cost
        target.add_health(8)
        return True