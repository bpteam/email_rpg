__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Personages.Warrior import Warrior
from src.Personages.Wizard import Wizard


class Hero(Warrior, Wizard):
    name = 'Герой'
    luck = 1
