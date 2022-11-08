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
    os.system("cls")
    print("Запустили новую игру из файла")

    player = ("Александр Чергов", 100, 100, 0)

    # запускаем главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")


        print("--Имя--")
        print(player[0])
        print("--Здоровье--")
        print(player[1])
        print("--Деньги--")
        print(player[2])
        print("--Зелья--")
        print(player[3])
        print("----------")

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
            player = shop.visit_shop(player)
        elif answer == "0":
            is_game = False
        elif answer == "4":
            print("ВЫ НАШЛИ ПАСХАЛКУ")
            print("Добавлена 08.11.22")
            print("--Паша гей--")
            input("чтобы завершить нажмите ENTER ")
            is_game = False
        elif answer == "18.08.2008":
            print("ВЫ НАШЛИ ПАСХАЛКУ")
            print("Добавлена 08.11.22")
            print("Дата рождение создателя этого кода")
            print("--Чеботарева Михаила Вадимовича--")
            input("чтобы завершить нажмите ENTER ")
            is_game = False
