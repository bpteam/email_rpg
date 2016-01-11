__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Game.Personages import Personage
from src.Game.Inventory import Sword
from src.Game.Inventory.Shield import Shield


class Warrior(Personage):
    weapon = Sword
    shield = False
    name = 'Воин'

    def get_attack(self):
        sword_buff = 0
        shield_buff = 0
        if isinstance(self.weapon, Sword):
            sword_buff = self.weapon.skill_effect
        if isinstance(self.shield, Shield):
            shield_buff = self.shield.skill_effect
        return super().get_attack() + sword_buff + shield_buff

    def equip_shield(self, shield):
        if isinstance(shield, Shield):
            self.shield = shield

    def equip_weapon(self, weapon):
        if isinstance(weapon, Sword):
            self.weapon = weapon
