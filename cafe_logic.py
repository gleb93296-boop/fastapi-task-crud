while True:
    x = input("Что делать? (1-Принять заказы/2-Выключить) ")
    if x == "2":
        break
    elif x == "1":
        stoll = int(input("Сколько столов нужно обслужить? "))
        for i in range(stoll):
            money = int(input(f"Какую сумму оставил стол №{i}? "))
            if money > 1000:
                print(f"Стол №{i} - это VIP-клиенты, дарим десерт!")
            elif money >= 500 and money <= 1000:
                print(f"Стол №{i} - хороший заказ, дарим кофе.")
            else:
                print(f"Стол №{i} - обычный заказ.")

