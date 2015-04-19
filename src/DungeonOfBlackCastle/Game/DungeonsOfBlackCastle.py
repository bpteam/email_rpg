__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Game.Game.Game import Game
from Game.Personages.Hero import Hero
from Game.Inventory.Gold import Gold
from DungeonOfBlackCastle.Inventory import Flask
from Game.Game.Dice import Dice
from Game.Game.DB import DB
from Game.Game.MessageText import MessageText


class DungeonsOfBlackCastle(Game):
    add_skill = 12
    add_health = 6
    add_luck = 6
    start_scene = 1
    hero = Hero()
    name = 'Подземелья темного замка'
    db = DB('DungeonsOfBlackCastle', 'email_rpg')
    global_commands = {
        'помощь': 'show_help',
        'выпить из фляги': 'drink_water',
        'положить .+': 'put_item',
        'выложить .+': 'drop_item'
    }

    def create(self):
        self.hero.max_health = Dice.throw(2) + self.add_health
        self.hero.health = self.hero.max_health
        self.hero.luck = Dice.throw() + self.add_luck
        self.hero.skill = Dice.throw() + self.add_skill
        self.hero.bag.put_items_to_bag([Gold({'count': 15}), Flask])
        self.current_scene = self.scene(self.start_scene)

    def save(self):
        data = {
            'user': self.user,
            'current_scene': self.current_scene,
            'previous_scene': self.previous_scene,
            'save_scenes': self.save_scenes,
            'hero': self.hero
        }
        self.db.save(data)

    @staticmethod
    def show_help():
        MessageText.add_text('help about game\n')

    def drink_water(self):
        flask = self.hero.bag.get_item_from_bag('фляга')
        if flask:
            flask.drink(self.hero)
            self.hero.bag.put_item_to_bag(flask)
        else:
            MessageText.add_text('Нет фляги\n')

    def put_item(self, name):
        item = self.current_scene.loot.get_item_from_bag(name)
        if item:
            self.hero.bag.put_item_to_bag(item)
            if item.count:
                self.current_scene.loot.put_item_to_bag(item)
        else:
            MessageText.add_text('Вещь не найдена\n')

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
                    MessageText.add_text('{0} ранит {1}\n'.format(attack_unit_name, target_unit_name))
                    target_unit.add_damage(fight_units.get(attack_unit_name).damage)
                    if target_unit.is_dead():
                        MessageText.add_text('{0} погибает\n'.format(target_unit_name))
                        if target_unit_name in alive_allies:
                            alive_allies -= {target_unit_name}
                        else:
                            alive_enemies -= {target_unit_name}
                        break

            complete_turn += 1
            if max_turn < complete_turn:
                break
