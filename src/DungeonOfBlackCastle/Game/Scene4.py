__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.DungeonOfBlackCastle.Game.MasterScene import MasterScene
from src.Game.Game.MessageText import MessageText
from src.DungeonOfBlackCastle.Spels.Levitation import Levitation
from src.DungeonOfBlackCastle.Spels.Swim import Swim


class Scene4(MasterScene):
    commands = {'к зданию в центре двора': 416, 'плавания': 372, 'левитации': 103, 'плавания и поплыть по течению реки': 311}

    def run(self):
        MessageText.add_text('Через несколько минут вы достигаете реки. На другом ее берегу разбиты палатки, горят костры, между которыми снуют Гоблины и Орки. Река подходит к высокому центральному строению и заканчивается у него, как дорога у ворот, но по шуму воды вы понимаете, что она небольшим водопадом стекает куда-то вниз, в подземелье.')
        if self.hero.has_manna_to_spell(Swim()) or self.hero.has_manna_to_spell(Levitation()):
            MessageText.add_text('Теперь вы можете вернуться обратно и направиться [к зданию в центре двора]')
            if self.hero.has_manna_to_spell(Swim()) and self.hero.has_manna_to_spell(Levitation()):
                MessageText.add_text('либо попытаться перебраться через реку (тогда вам надо решить, каким заклятием вы воспользуетесь: [плавания] или [левитации]),')
            if self.hero.has_manna_to_spell(Swim()):
                MessageText.add_text('либо воспользоваться заклятием [плавания и поплыть по течению реки], чтобы проникнуть в подземелье замка.')
        else:
            MessageText.add_text('Теперь вы можете вернуться обратно и направиться [к зданию в центре двора]')
            return self.commands.get('к зданию в центре двора')