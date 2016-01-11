__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Game.Personages import Warrior
from src.Game.Personages.Wizard import Wizard


class Hero(Warrior, Wizard):
    name = 'Герой'
    luck = 1
    min_luck = 1

    def add_luck(self, luck=1):
        self.luck += luck

    def remove_luck(self, luck=1):
        if self.luck >= self.min_luck:
            self.luck -= luck