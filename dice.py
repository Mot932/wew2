import random
import makecart

def play_casino():
    
    player = ("Александр Чергов", 100, 100, 0)


user_money = hero[3]
casino_money = 100

while user_money and casino_money:

    print("у игрока", user_money, "money")
    print("у казино", casino_money, "money")

    input("Нажмите ENTER чтобы сделать ход")
    
    user_turn = random.randint(1, 6)
    casino_turn = random.randint(1, 6)  
    print("игрок выбросил", user_turn)
    print("казино выбросил", casino_turn)



    if user_turn > casino_turn:
        print ("игрок победил")
        user_money += 5000
        casino_money -= 5000
    elif casino_turn > user_turn:
        print("казино победило")
        user_money -= 5000
        casino_money += 5000
    else:
        print("ничья")

if casino_money == 0:
    print("Игрок забрал все деньги")
else:
    print("казино забрала все деньги")
play_casino(player)