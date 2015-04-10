__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Personages.Warrior import Warrior
from src.Personages.Wizard import Wizard


class Hero(Warrior, Wizard):
    name = 'Герой'
    luck = 1
