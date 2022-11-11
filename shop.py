import os
import makecart

def visit_shop(player):
    
    hp = player[1]
    money = player[2]
    potions = player[6]

    is_shop = True
    while is_shop:
        os.system("cls")
        print("--деньги--")
        print(money)
        print("--зелья--")
        print(potions)
        print("--Варианты")
        print("1 - купить зелье")
        print("2 - уйти")


        answer = input("Введите номер варианта и нажмите ENTER! ")
        if answer == "1":
            os.system("cls")
            if money >= 100:
                money -= 100
                potions += 1
                print(f"{player[0]} купил зелье")
            else:
                print("У ВАС НЕТ ДЕНЕГ!!!")
        elif answer == "2":
            return(player[0], player[1], player[2],player[3], player[5], money, potions)
