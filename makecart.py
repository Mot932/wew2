import random


first_names = ("Жран", "Дрын", "Брысь", "Жлыг", "Паша")
last_name = ("Ужасный", "Зловонный", "Борзый", "Жирный", "Кровавый")


def make_hero(
		name=None, 
		hp=None, 
		xp=None, 
		attack=None, 
		defence=None, 
		money=None, 
		potions=None
) -> tuple:
	if not name:
		name = f"{random.choice(first_names)} {random.choice(last_name)}"
	if not hp:
		hp = random.randint(1, 100)
	if not xp:
		xp = random.randint(0, 100)
	if not attack:
		attack = random.randint(1, 100)
	if not defence:
		defence = random.randint(0, 100)
	if not money:
		money = random.randint(1, 1000)
	if not potions:
		potions = random.randint(0, 1)

	return (name, hp, xp, attack, defence, money, potions)


def show_hero(hero:tuple):
	print("Имя", hero[0])
	print("Здоровье", hero[1])
	print("Умение", hero[2])
	print("Деньги", hero[3])
	print("Атака", hero[4])
	print("Защита", hero[5])
	print("Зелья", hero[6])

