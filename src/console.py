__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from DungeonOfBlackCastle.Game.DungeonsOfBlackCastle import DungeonsOfBlackCastle
from Game.Game.MessageText import MessageText

user = 'test@user.net'
game = DungeonsOfBlackCastle()

game.user = input('Ваш email:')

if not game.db.game_exist(user):
    game.create()
else:
    game.load()

command = False
while not game.is_end():
    game.scene(game.current_scene.number, command)
    MessageText.show_text()
    if not game.is_end():
        command = input('ваш ответ:')