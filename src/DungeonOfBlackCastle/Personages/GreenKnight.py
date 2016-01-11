__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Game.Personages import Warrior
from src.Game.Personages.Wizard import Wizard


class GreenKnight(Wizard, Warrior):
    name = 'Зеленый рыцарь'

    def exposure_of_spell(self, caster, spell):
        """
        :param caster Wizard:
        :param spell Spell:
        :return:
        """
        self.cast_spell(spell, caster)