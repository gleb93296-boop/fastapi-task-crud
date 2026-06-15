def speed(second):
    return second - 5
runes = []
profi = []
while True:
    time = int(input("Введите время бегуна: "))
    if time <= 0:
        break
    runes.append(time)
for ru in runes:
    if ru < 60:
        x = speed(ru)
        profi.append(x)
print(profi)