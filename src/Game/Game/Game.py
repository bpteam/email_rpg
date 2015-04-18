__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractproperty, abstractmethod
from Game.DB import DB


class Game(metaclass=ABCMeta):
    current_scene = 1
    text = ''
    history = []
    user = 'user@my.game'
    end_game = False

    def start_scene(self):
        self.scene(1)

    @abstractproperty
    def name(self):
        pass

    def __init__(self, **data):
        """
        :param data:
        :return:
        """
        self.user = data['user']
        self.create()
        self.start_scene()

    @staticmethod
    def create():
        pass

    @abstractmethod
    def scene(self, paragraph, answer=False):
        pass

    def add_text(self, text):
        self.text += text

    def show_text(self):
        print(self.text)
        self.text = ''

    @abstractmethod
    def end(self):
        pass

    def is_end(self):
        return self.end_game