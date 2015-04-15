__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Personages.Warrior import Warrior
from Personages.Wizard import Wizard


class Hero(Warrior, Wizard):
    name = 'Герой'
    luck = 1
