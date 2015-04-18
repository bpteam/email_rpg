__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from Game.Game.Scene import Scene


class CustomScene(Scene):

    default_commands = {
        'помощь': 'show_help',
        'выпить из фляги': 'drink_water',
        'положить .+': 'put_item',
        'выложить .+': 'drop_item'
    }

    def __init__(self, previous, command=False):
        pass

    def run(self):
        pass