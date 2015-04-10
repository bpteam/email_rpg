__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from src.Inventory.Thing import Thing


class Flask(Thing):
    name = 'фляга'
    size = 0
    count = 2
    max_stack = 2

    def drink(self, personage):
        if self.use(1):
            personage.add_health(2)

    def fill(self, count=2):
        self.stack_item(count)