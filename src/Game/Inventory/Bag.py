__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Game.Inventory import Thing


class Bag(Thing):

    name = 'мешок'
    max_size = 7
    items = []

    def __init__(self, *items):
        """
        :param items (list):
        :return:
        """
        self.put_items_to_bag(items)

    def put_items_to_bag(self, items):
        """
        :param items (list):
        :return:
        """
        for item in items:
            if self.has_space(item):
                self.put_item_to_bag(item)

    def put_item_to_bag(self, item):
        if isinstance(item, Thing):
            if self.has_item(item.name):
                item_from_bag = self.get_item_from_bag(item.name)
                item.count = item_from_bag.stack_item(item.count)
                self.put_item_to_bag(item_from_bag)
            if self.has_space(item) and item.count:
                self.items.insert(0, item)
            return True
        else:
            return False

    def get_item_from_bag(self, name):
        index = self.find_item(name)
        if isinstance(index, int):
            item = self.items.pop(index)
            return item
        else:
            return False

    def get_size(self):
        size = 0
        for item in self.items:
            size += item.get_size
        return size

    def has_space(self, item):
        return (item.get_size() + self.get_size()) <= self.max_size

    def has_item(self, name):
        return isinstance(self.find_item(name), int)

    def find_item(self, name):
        for index, item in self.items:
            if item.name == name:
                return index
        return False

    @staticmethod
    def move_item(item, source, target):
        if isinstance(item, str):
            item = source.get_item_from_bag(item)
        else:
            item = source.get_item_from_bag(item.name)
        if target.put_item_to_bag(item):
            return True
        else:
            source.put_item_to_bag(item)
            return False