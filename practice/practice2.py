import math

# Функція, задана частинами
def f(x):
    if x < -1:
        return math.acos((math.pi - x) / 2)
    elif -1 < x < 1:
        return math.exp(-x**2)
    elif x == 1:
        return 10**-3
    elif x > 1:
        return math.pi * (math.log(x)**2)
    else:
        return None

# Введення даних
x_start = float(input("Введіть початкове значення аргументу: "))
x_end = float(input("Введіть кінцеве значення аргументу: "))
step = float(input("Введіть крок зміни аргументу: "))

print("\nОбчислення значень функції:")
print(f"{'№':<5}{'x':<15}{'y=f(x)':<20}{'Пояснення':<30}")

i = 1
x = x_start

while x <= x_end:
    y = f(x)
    
    # Пояснення, яку саме частину функції використано
    if x < -1:
        note = "arccos((π-x)/2)"
    elif -1 < x < 1:
        note = "exp(-x^2)"
    elif x == 1:
        note = "10^-3"
    elif x > 1:
        note = "π*(ln(x))^2"
    else:
        note = "не визначено"
    
    print(f"{i:<5}{x:<15.6f}{y:<20.6f}{note:<30}")
    
    x += step
    i += 1
