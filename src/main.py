__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Game.DB import DB
from DungeonOfBlackCastle.Game.DungeonsOfBlackCastle import DungeonsOfBlackCastle

user = 'test@user.net'
storage = DB('DungeonsOfBlackCastle')

if not storage.game_exist(user):
    game = DungeonsOfBlackCastle.create()
else:
    game = storage.load(user)