__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Game.Game.Scene import Scene
from Game.Game.MessageText import MessageText


class Scene1(Scene):
    commands = {'': 1}

    def run(self):
        MessageText.add_text('')