# -*- coding: utf-8 -*-

import random

class Personage(): # общие персонажи

	def __init__(self, name, skill, damage, gold = 0): # начальные значения
		self.name = name
		self.skill = skill
		self.damage = damage
		self.gold = gold

	def fight(self):
		pass
		
class Protagonist(Personage): # главный герой

	def __init__(self, name, skill, damage, gold, fortune, **spell): # необходимо добавить заклятия
		Personage.__init__(self, name, damage, skill, gold)
		self.fortune = fortune
		self.spell = spell
		self.bag = []
		self.flask = 2 # фляга, из которой можно пополнить выносливость 2 раза
		
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

# проверка			
if __name__ == "__main__":
	r_skill = random.randint(1, 6) + 6
	r_damage = random.randint(1, 12) + 12
	r_fortune = random.randint(1, 6) + 6
	protagonist = Protagonist("герой", r_skill, r_damage, 15, r_fortune, lev="заклятие левитации", power="заклятие силы")
	print("%s:\n мастерство - %d,\n выносливость - %d,\n удача - %d" % (protagonist.name,  
	                            protagonist.skill, protagonist.damage, protagonist.fortune))
	print(protagonist.spell)
	protagonist.bag_to_place("перо аиста")
	print(protagonist.bag)
	protagonist.bag_shell_out("перо аиста")
	print(protagonist.bag)
	protagonist.flask_out()
	print("отпил из фляги выносливость стала %s" % (protagonist.damage))
	
	