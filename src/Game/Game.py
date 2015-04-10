__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractproperty, abstractmethod


class Game(metaclass=ABCMeta):
    current_paragraph = 1
    text = ''
    history = []

    def __init__(self, **save):
        if not save:
            self.create()
        else:
            self.scene(save)

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def scene(self, **parts):
        pass

    @abstractmethod
    def redirect(self, paragraph):  # авто перенаправление пользователя на другой параграф
        pass

    def add_text(self, text):
        self.text += text

