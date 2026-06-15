while True:
    programma = input("Открыть вход для группы? (да/выход) ")
    if programma == "выход":
        print("Система отключена")
        break
    elif programma == "да":
        people = int(input("Сколько человек в группе на входе? "))
        for i in range(people):
            age = int(input("Сколько тебе лет? "))
            if age >= 18:
                print(f"Доступ разрешён, №{i + 1}")
            elif age >= 14 and age <= 17:
                print(f"Требуется разрешение от родителей, №{i + 1}")
            elif age < 14:
                print(f"Доступ запрещён, №{i + 1}")