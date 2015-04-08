__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from abc import ABCMeta, abstractproperty  # , abstractmethod


class Thing(metaclass=ABCMeta):

    @abstractproperty
    def name(self):
        pass
    size = 1
    count = 1
    max_stack = 1

    def __init__(self, **attributes):
        for name in attributes.keys():
            self.__setattr__(self, name, attributes.get(name))

    def get_size(self):
        return self.size

    def use(self, count):
        if self.can_use(count):
            self.count -= count
            return True
        else:
            return False

    def can_use(self, need=1):
        return self.count >= need