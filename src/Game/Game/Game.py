__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from abc import ABCMeta, abstractproperty
from Game.Game.DB import DB
from Game.Game.MessageText import MessageText
import re


class Game(metaclass=ABCMeta):
    current_scene = None
    previous_scene = 1
    start_scene = 1
    text = ''
    history = []
    save_scenes = {}
    user = 'user@my.game'
    end_game = False
    db = DB()
    global_commands = {
        'help': 'show_help',
        'drink water': 'drink_water',
        'put (?P<arg>.+)': 'put_item',
        'drop (?P<arg>.+)': 'drop_item'
    }

    @abstractproperty
    def name(self):
        pass

    def __init__(self):
        pass

    def create(self):
        pass

    def load(self):
        if self.db.game_exist(self.user):
            data = self.db.load(self.user)
            for name, value in data:
                self.__setattr__(name, value)

    def save(self):
        pass

    def scene(self, paragraph, command=False):
        if paragraph in self.save_scenes.keys():
            self.current_scene = self.save_scenes.get(paragraph)
            self.current_scene.command = command
        else:
            self.current_scene = eval('Scene%d' % paragraph)(paragraph, command)
        self.global_run(command)
        self.current_scene.run()

    def global_run(self, command):
        for glob_command, method in self.global_commands:
            regexp = re.compile(glob_command)
            match = regexp.search(command)
            if match.group():
                if match.group('arg'):
                    eval('self.{0}'.format(method))(match.group('arg'))
                else:
                    eval('self.{0}'.format(method))()

    def save_scene(self, scene):
        self.save_scenes.update({scene.number: scene})

    def end(self):
        self.end_game = True
        MessageText.add_text('Game Over\n')

    def is_end(self):
        return self.end_game