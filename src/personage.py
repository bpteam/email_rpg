# -*- coding: utf-8 -*-

import random


class Personage():  # общие персонажи

    def __init__(self, name, skill, damage, gold=0):  # начальные значения
        self.name = name
        self.skill = skill
        self.damage = damage
        self.gold = gold

    def fight(self):
        pass


class Protagonist(Personage):  # главный герой

    def __init__(self, name, skill, damage, gold, fortune, **spell):  # необходимо добавить заклятия
        Personage.__init__(self, name, damage, skill, gold)
        self.fortune = fortune
        self.spell = spell
        self.bag = []
        self.flask = 2  # фляга, из которой можно пополнить выносливость 2 раза

    def bag_to_place(self, artefact):
        if len(self.bag) <= 7:
            self.bag.append(artefact)
            return self.bag
        else:
            print("нужно что-то выложить")
            return self.bag

    def bag_shell_out(self, artefact):
        self.bag.remove(artefact)
        return self.bag

    def flask_out(self):
        if self.flask > 0:
            self.flask -= 1
            self.damage += 2
        else:
            print("фляга пуста.")


def fight(protagonist, *args):
    hero = protagonist
    list_rival = list(args)  # список передаваемых экземпляров
    while True:
        power_hit_rivals = {}

        r_val_protagonist = random.randint(1, 12)  # случайное значение для главного героя(имитация броска 2 кубиков)
        power_hit_protagonist = r_val_protagonist + hero.skill  # сила удара главного героя

        for rival in list_rival:
            r_val_rival = random.randint(1, 12)  # случайное значение для каждого персонажа
            power_hit_rivals[rival.name] = r_val_rival + rival.skill  # сила удара персонажа

        if len(power_hit_rivals) > 1:  # если бой не с одним персонажем, то идет опрос с кем драться
            print("кого из соперников будете атаковать?")
            for x in power_hit_rivals.keys():
                for y in list_rival:
                    if y.name == x:  # ищем с кем идет бой
                        skill_rival = y.skill  # мастерство того, на кого направлена атака
                        damage_rival = y.damage  # выносливость того, на кого направлена атака
                print("%s: выносливость - %d , мастерство - %d" % (x, damage_rival, skill_rival))

        else:  # если бой только с одним персонажем
            r_val_rival = random.randint(1, 12)
            power_hit_rival = list_rival[0].skill + r_val_rival  # сила удара персонажа

            if power_hit_protagonist > power_hit_rival:
                list_rival[0].damage -= 2
                if list_rival[0].damage <= 0:
                    print("%s убит" % list_rival[0].name)
                    print("ваша выносливость - %s" % protagonist.damage)
                    break

            elif power_hit_protagonist < power_hit_rival:
                protagonist.damage -= 2
                if protagonist.damage <= 0:
                    print("вы убиты")
                    break
            continue

        atak = input("введите кого будете атаковать:")  # добавить проверку что введено
        if power_hit_rivals[atak] > power_hit_protagonist:
            hero.damage -= 2
            print("ваша выносливость - %d" % (hero.damage))
        else:
            for y in list_rival:
                if y.name == atak:
                    if y.damage <= 2:
                        print("%s убит" % atak)
                        list_rival.remove(y)
                    else:
                        y.damage -= 2
                        print("ваша выносливость - %d" % (hero.damage))
                    # необходима проверка остальные персонажи нанели урон или их удар был парирован


# проверка			
if __name__ == "__main__":
    r_skill = random.randint(1, 6) + 6
    r_damage = random.randint(1, 12) + 12
    r_fortune = random.randint(1, 6) + 6
    protagonist = Protagonist("герой", r_skill, r_damage, 15, r_fortune, lev="заклятие левитации",
                              power="заклятие силы")
    print("%s:\n мастерство - %d,\n выносливость - %d,\n удача - %d" % (protagonist.name,
                                                                        protagonist.skill, protagonist.damage,
                                                                        protagonist.fortune))
    print(protagonist.spell)
    protagonist.bag_to_place("перо аиста")
    print(protagonist.bag)
    protagonist.bag_shell_out("перо аиста")
    print(protagonist.bag)
    protagonist.flask_out()
    print("отпил из фляги выносливость стала %s" % (protagonist.damage))
    ork = Personage("орк1", 17, 7)
    ork_1 = Personage("орк2", 16, 5)
    spider = Personage("паук", 10, 5)
    fight(protagonist, ork_1, spider)
    vod = Personage("водяной", 13, 9)
    fight(protagonist, ork, vod)