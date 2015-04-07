__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Inventory.Thing import Thing


class Bag(Thing):

    name = 'мешок'
    max_size = 7
    items = {}

    def __init__(self, items):
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
        if self.has_space(item):
            self.items.update({item.name: item})
            return True
        else:
            return False

    def get_item_from_bag(self, name):
        if self.has_item(name):
            item = self.items.get(name)
            del self.items[name]
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
        return name in self.items


