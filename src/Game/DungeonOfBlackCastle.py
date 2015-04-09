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
    def fight(allies, enemies, max_turn=0):
        """
        :param allies {}:
        :param enemies {}:
        :return:
        """
        from collections import OrderedDict
        alive_allies = set()
        alive_enemies = set()
        for ally in allies:
                alive_allies.add(ally.name)
        for enemy in enemies:
                alive_enemies.add(enemy.name)

        complete_turn = 0
        while alive_allies and alive_enemies:
            fight_units = {}
            for ally in allies:
                fight_units.update({ally.name: ally.get_attack()})
            for enemy in enemies:
                fight_units.update({enemy.name: enemy.get_attack()})
            fight_units = OrderedDict(sorted(fight_units.items(), key=lambda t: t[1], reverse=True))

            for attack_unit_name in list(fight_units.keys()):
                attack_unit_skill = fight_units.get(attack_unit_name)
                if attack_unit_name in alive_allies:
                    target_unit_name = alive_enemies[0]
                else:
                    target_unit_name = alive_allies[0]
                target_unit = fight_units.get(target_unit_name)  # todo fix me wrong data, need Presonage, get integer
                target_unit_skill = fight_units.get(target_unit_name)
                if attack_unit_skill > target_unit_skill:
                    target_unit.add_damage(fight_units.get(attack_unit_name).damage)
                    if target_unit.is_dead():
                        if target_unit_name in alive_allies:
                            alive_allies -= {target_unit_name}
                        else:
                            alive_enemies -= {target_unit_name}
                        break

            complete_turn += 1
            if max_turn < complete_turn:
                break
