__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Personages.Hero import Hero
from src.Game.Dice import Dice
from src.Inventory.Gold import Gold
from src.Inventory.Flask import Flask


class Game(object):
    add_skill = 12
    add_health = 6
    add_luck = 6
    hero = Hero()
    current_paragraph = 1
    text = ''

    def __init__(self, **save):
        if not save:
            self.create()
        else:
            self.scene(save)

    def create(self):
        self.hero.max_health = Dice.throw(2) + Game.add_health
        self.hero.health = self.hero.max_health
        self.hero.luck = Dice.throw() + Game.add_luck
        self.hero.skill = Dice.throw() + Game.add_skill
        self.hero.bag.put_items_to_bag([Gold({'count': 15}), Flask])

    def scene(self, **parts):
        pass

    def redirect(self, paragraph):  # авто перенаправление пользователя на другой параграф
        pass

    def fight(self, allies, enemies):
        pass
