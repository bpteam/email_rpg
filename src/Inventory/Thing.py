__author__ = 'iEC'

from abc import ABCMeta, abstractproperty  # , abstractmethod


class Thing(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass
    size = 1
    max_stack = 1

    def get_size(self):
        return self.size
