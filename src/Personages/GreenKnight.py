__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Personages.Warrior import Warrior
from src.Personages.Wizard import Wizard


class GreenKnight(Wizard, Warrior):
    name = 'Зеленый рыцарь'

    def exposure_of_spell(self, caster, spell):
        """
        :param caster Wizard:
        :param spell Spell:
        :return:
        """
        self.cast_spell(spell, caster)