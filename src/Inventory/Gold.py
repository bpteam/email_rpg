__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Inventory.Thing import Thing


class Gold(Thing):
    name = 'золото'
    max_stack = 99
    size = 0