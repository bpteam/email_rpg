__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Game.Game.Scene import Scene
from Game.Game.MessageText import MessageText
from Game.Personages.Warrior import Warrior
from Game.Inventory.Bag import Bag
from Game.Inventory.Gold import Gold
from DungeonOfBlackCastle.Spels.Copy import Copy


class Scene6(Scene):
    commands = {'': 1}
    first_woodcutter = Warrior(name='Тин дровосек', skill=5, health=4, bag=Bag(Gold(count=1)))
    second_woodcutter = Warrior(name='Эукариот дровосек', skill=6, health=7)
    ally_copy = None
    need_save = True

    def run(self):
        if not self.first_woodcutter.is_dead() and not self.second_woodcutter.is_dead():
            MessageText.add_text('Сражаться с двумя Дровосеками вам придется одновременно.\n')
            if self.hero.has_manna_to_spell(Copy()):
                MessageText.add_text('Вы можете воспользоваться заклятием [Копии] или [начать бой].')

    def cast_copy(self):
        self.ally_copy = self.hero.cast_spell(Copy(), self.second_woodcutter)