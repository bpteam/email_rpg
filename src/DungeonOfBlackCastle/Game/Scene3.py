__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.DungeonOfBlackCastle.Game.MasterScene import MasterScene
from src.Game.Game.MessageText import MessageText


class Scene3(MasterScene):
    commands = {'more': 211}

    def run(self):
        MessageText.add_text('Вы рады, что дорога привела вас к Беглецам, и понимаете, что Черный замок должен быть где-то неподалеку. Напоследок лес делает все, чтобы удержать вас: сучья цепляются за одежду, ветви хлещут по лицу, корни и коряги как будто вылезли из земли погреться и заставляют вас идти медленно и осторожно. Вдруг впереди забрезжил свет. Но как же он отличается от яркого весеннего солнца, которое светило, когда вы только-только входили в Зачарованный лес! Облака плотно закрыли солнце и пропускают лишь неясное и бледное свечение. Однако видно все же достаточно хорошо, и вы с облегчением покидаете негостеприимный лес.\n')
        return self.commands.get('more')
