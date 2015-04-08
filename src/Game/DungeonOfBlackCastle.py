__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'

from src.Game.Game import Game
from src.Personages.Hero import Hero
from src.Inventory.Gold import Gold
from src.Inventory.Flask import Flask
from src.Game.Dice import Dice


class DungeonOfBlackCastle(Game):
    add_skill = 12
    add_health = 6
    add_luck = 6
    hero = Hero

    def create(self):
        self.hero.max_health = Dice.throw(2) + self.add_health
        self.hero.health = self.hero.max_health
        self.hero.luck = Dice.throw() + self.add_luck
        self.hero.skill = Dice.throw() + self.add_skill
        self.hero.bag.put_items_to_bag([Gold({'count': 15}), Flask])

    @staticmethod
    def fight(allies, enemies):
        """
        :param allies (list):
        :param enemies (list):
        :return:
        """
        from collections import OrderedDict
        group_allies = {}
        group_enemies = {}
        for ally in allies:
            group_allies.update({ally.name: ally})
        for enemy in enemies:
            group_enemies.update({enemy.name: enemy})

        while group_allies and group_enemies:
            fight_units = group_allies.copy()
            fight_units.update(group_enemies)
            for unit in fight_units.keys():
                fight_units.update({unit: group_enemies.get(unit).get_attack()})
            fight_units = OrderedDict(sorted(fight_units.items(), key=lambda t: t[1], reverse=True))
            for attack_unit_name in list(fight_units.keys()):
                attack_unit = fight_units.get(attack_unit_name)
                if attack_unit_name in group_allies.keys():
                    target_unit_name = list(group_enemies.keys())[0]
                else:
                    target_unit_name = list(group_allies.keys())[0]
                target_unit = fight_units.get(target_unit_name)
                if attack_unit > target_unit:
                    group_enemies.get(target_unit_name).add_damage(group_allies.get(attack_unit_name).damage)
