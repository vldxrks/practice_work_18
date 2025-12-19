import math

#Обчислення значення функції
def f(x, n):
    if n == 1:
        return math.sin(x)
    elif n == 2:
        return math.cos(x)
    elif n == 3:
        return math.exp(x)
    elif n == 4:
        return x ** 2
    else:
        return 0

#Табулювання
def tabulate():
    print("\nОберіть функцію:")
    print("1 - sin(x), 2 - cos(x), 3 - e^x, 4 - x^2")
    n = int(input("Ваш вибір: "))
    a = float(input("Початок відрізку a: "))
    b = float(input("Кінець відрізку b: "))
    h = float(input("Крок h: "))

    print("\nТаблиця значень:")
    x = a
    while x <= b + 1e-9:
        print(f"x = {x:.2f}\tf(x) = {f(x, n):.6f}")
        x += h

#Метод Сімпсона
def simpson():
    print("\nОберіть функцію:")
    print("1 - sin(x), 2 - cos(x), 3 - e^x, 4 - x^2")
    n = int(input("Ваш вибір: "))
    a = float(input("Початок відрізку a: "))
    b = float(input("Кінець відрізку b: "))
    m = int(input("Кількість підінтервалів m (парне число): "))

    if m % 2 != 0:
        print("m має бути парним, змінюємо на", m + 1)
        m += 1

    h = (b - a) / m
    s = f(a, n) + f(b, n)
    for i in range(1, m):
        x = a + i * h
        s += f(x, n) * (4 if i % 2 else 2)
    result = s * h / 3
    print(f"\nІнтеграл ≈ {result:.6f}")

#Головне меню
while True:
    print("\n=== МЕНЮ ===")
    print("1. Табулювання функції")
    print("2. Обчислення інтегралу (метод Сімпсона)")
    print("3. Вихід")
    choice = input("Ваш вибір: ")

    if choice == "1":
        tabulate()
    elif choice == "2":
        simpson()
    elif choice == "3":
        print("Роботу завершено.")
        break
    else:
        print("Невірний вибір! Спробуйте ще раз.")
