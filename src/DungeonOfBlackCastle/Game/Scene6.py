__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.DungeonOfBlackCastle.Game.MasterScene import MasterScene
from src.DungeonOfBlackCastle.Game.DungeonsOfBlackCastle import DungeonsOfBlackCastle
from src.Game.Game.MessageText import MessageText
from src.Game.Personages.Warrior import Warrior
from src.Game.Inventory.Bag import Bag
from src.Game.Inventory.Gold import Gold
from src.DungeonOfBlackCastle.Spels.Copy import Copy
from src.DungeonOfBlackCastle.Personages.PersonageCopy import PersonageCopy


class Scene6(MasterScene):
    commands = {'Копия(?P<arg>.*)': 'cast_copy', 'начать бой': 'fight', 'дальше': 420}
    first_woodcutter = Warrior(name='Тин дровосек', skill=5, health=4, bag=Bag(Gold(count=1)))
    second_woodcutter = Warrior(name='Борис дровосек', skill=6, health=7)
    ally_copy = None
    need_save = True

    def run(self):
        if not self.first_woodcutter.is_dead() and not self.second_woodcutter.is_dead():
            MessageText.add_text('Сражаться с двумя Дровосеками вам придется одновременно.\n')
            if self.hero.has_manna_to_spell(Copy()) and not bool(self.ally_copy):
                MessageText.add_text('Вы можете воспользоваться заклятием [Копия] или [начать бой].')
        if self.first_woodcutter.is_dead() and self.second_woodcutter.is_dead():
            self.hero.remove_luck(1)
            MessageText.add_text('Вы победили дровосеков, наградой вам будет всего 1 золотой в кармане Первого дровосека. Дровосеки люди небогатые, и вряд ли стоило убивать их. Теперь отправляйтесь [дальше]')
            self.hero.bag.put_item_to_bag(Gold({'count': 1}))
            return self.commands.get('дальше')

    def cast_copy(self):
        self.ally_copy = self.hero.cast_spell(Copy(), self.second_woodcutter)

    def fight(self):
        if isinstance(self.ally_copy, PersonageCopy):
            ally = [self.hero, self.ally_copy]
        else:
            ally = [self.hero]
        DungeonsOfBlackCastle.fight(ally, [self.first_woodcutter, self.second_woodcutter])