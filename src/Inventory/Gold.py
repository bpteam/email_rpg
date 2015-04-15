__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Inventory.Thing import Thing


class Gold(Thing):
    name = 'золото'
    max_stack = 999
    size = 0