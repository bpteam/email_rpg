__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from abc import ABCMeta, abstractproperty, abstractmethod


class Game(metaclass=ABCMeta):
    current_paragraph = 1
    text = ''

    def __init__(self, **save):
        if not save:
            self.create()
        else:
            self.scene(save)

    @abstractmethod
    def create(self):
        pass

    def scene(self, **parts):
        pass

    def redirect(self, paragraph):  # авто перенаправление пользователя на другой параграф
        pass

    def add_text(self, text):
        self.text += text

