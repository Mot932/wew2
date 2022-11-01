import os
import shop



def start_new_game():
    """
    Создает персонаж:
        Имя
        Здоровье
        деньги
        зелья
    """
    print("Запустили новую игру из файла")

    player = ("Александр Чергов", 100, 100, 0)


    # запускаем главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")

        player = ("Александр Чергов", 100, 100, 0)

        print("-- ситуация:")
        print(f"{player[0]} приехал к камню.")
        print("-- варианты:")
        print("1 - поехать на битву")
        print("2 - поехать играть в кости")
        print("3 - поехать в лавку к ведьме")
        print("0 - выйти в главное меню")


        answer = input("Введите номер варианта и нажмите ENTER! ")
        if answer == "1":
            pass
        elif answer == "2":
            pass
        elif answer == "3":
            shop.visit_shop(player)
        elif answer == "0":
            is_game = False