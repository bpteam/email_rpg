__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from pymongo import MongoClient


class DB:
    def __init__(self, game='DungeonsOfBlackCastle', db_name='email_rpg'):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db_name]
        self.game = self.db[game]

    def load(self, user_name):
        return self.game.find_one(user_name, {'user': user_name, 'active': True})

    def save(self, game):
        """
        :param game(dict):
        :return:
        """
        self.game.update(game.get('user'), game)

    def game_exist(self, user_name):
        return self.game.count({'user': user_name, 'active': True}) > 0

    def close(self, user_name):
        return self.game.find_one_and_update(user_name, {'user': user_name, 'active': True}, {'active': False})