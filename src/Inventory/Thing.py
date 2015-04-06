__author__ = 'iEC'

from abc import ABCMeta, abstractproperty  # , abstractmethod


class Thing(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass
    size = 1
    count = 1
    max_stack = 1

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