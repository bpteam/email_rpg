__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Personages.Personage import Personage


class Wizard(Personage):
    manna = 10
    name = 'Колдун'

    def cast_spell(self, spell, target):
        """
        :param spell:
        :param target Personage:
        :return bool|:
        """
        if self.has_manna_to_spell(spell):
            return target.exposure_of_spell(self, spell)
        else:
            return False

    def has_manna_to_spell(self, spell):
        return self.manna >= spell.manna_cost