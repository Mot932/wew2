import os



def visit_shop(player):
    """
    печатаем песронажа
    покупаем зелья тратим деньги
    варианты:
        Купить зелье(цена)
        обратно
    """

    input()

    is_shop = True
    while is_shop:
        os.system("cls")
        player = ("Александр Чергов", 100, 100, 0)
        print("--Варианты")
        print("1 - купить зелье")
        print("2 - уйти")


        answer = input("Введите номер варианта и нажмите ENTER! ")
        if answer == "1":
            os.system("cls")
            if player[2] >= 100:
                player[2] -= 100
                player[3] += 1
                print(f"{player[0]} купил зелье")
            else:
                print("У ВАС НЕТ ДЕНЕГ!!!")
        elif answer == "2":
            player = shop.visit_shop(player)
