__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.DungeonOfBlackCastle.Game.MasterScene import MasterScene
from src.Game.Game.MessageText import MessageText


class Scene5(MasterScene):
    commands = {'к острову': 216, 'на другой берег': 517}

    def run(self):
        MessageText.add_text('Куда вы поплывете — [к острову] или [на другой берег] ?')