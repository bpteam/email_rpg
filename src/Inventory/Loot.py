__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Inventory.Bag import Bag


class Loot(Bag):
    name = 'добыча'
    max_size = 999