__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractproperty, abstractmethod


class Game(metaclass=ABCMeta):
    current_paragraph = 1
    text = ''
    history = []
    user = 'user@my.game'

    @abstractproperty
    def start_scene(self):
        pass

    def __init__(self, data=None):
        """
        :param data:
        :return:
        """
        if not data:
            self.create()
        else:
            self.scene(data)

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def scene(self, data):
        pass

    def add_text(self, text):
        self.text += text

    def show_text(self):
        print(self.text)
        self.text = ''

    @abstractmethod
    def end(self):
        pass