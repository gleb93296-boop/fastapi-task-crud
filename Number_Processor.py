def slozhenie(number):
    x = number + 10
    return x
numbers = []
numbers2 = []
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    numbers.append(num)
for bers in numbers:
        if bers % 2 == 0:
            x = slozhenie(bers)
            numbers2.append(x)
print(numbers2)
