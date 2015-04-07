__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Personages.Personage import Personage
from src.Inventory.Sword import Sword


class Warrior(Personage):
    Weapon = Sword()
    name = 'Воин'