__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Game.Game import Game
from Game.Personages.Hero import Hero
from Game.Inventory.Gold import Gold
from DungeonOfBlackCastle.Inventory import Flask
from Game.Game.Dice import Dice


class DungeonsOfBlackCastle(Game):
    add_skill = 12
    add_health = 6
    add_luck = 6
    start_scene = 1
    hero = Hero
    name = 'Подземелья темного замка'

    @staticmethod
    def create():
        game = DungeonsOfBlackCastle
        game.hero.max_health = Dice.throw(2) + game.add_health
        game.hero.health = game.hero.max_health
        game.hero.luck = Dice.throw() + game.add_luck
        game.hero.skill = Dice.throw() + game.add_skill
        game.hero.bag.put_items_to_bag([Gold({'count': 15}), Flask])
        game.current_scene = game.start_scene
        return game

    @staticmethod
    def fight(allies, enemies, max_turn=0):
        """
        :param allies {}:
        :param enemies {}:
        :return:
        """
        from collections import OrderedDict
        units = {}
        alive_allies = set()
        alive_enemies = set()
        for ally in allies:
            alive_allies.add(ally.name)
            units.update({ally.name: ally})
        for enemy in enemies:
            alive_enemies.add(enemy.name)
            units.update({enemy.name: enemy})

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
                target_unit = units.get(target_unit_name)
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
