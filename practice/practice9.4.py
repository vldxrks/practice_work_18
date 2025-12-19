# Введення двоцифрового числа
n = int(input("Введіть двоцифрове число: "))

if 10 <= abs(n) <= 99:
    tens = abs(n) // 10
    ones = abs(n) % 10
    s = tens + ones
    p = tens * ones
    print(f"Десятків: {tens}")
    print(f"Одиниць: {ones}")
    print(f"Сума цифр: {s}")
    print(f"Добуток цифр: {p}")
else:
    print("Це не двоцифрове число!")
