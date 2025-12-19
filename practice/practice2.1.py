import math

# Функція
def f(x):
    return (x**3 - 2) / (3 * math.log(x))

# Ввід даних
x_start = float(input("Введіть початкове значення x: "))
x_end = float(input("Введіть кінцеве значення x: "))
step = float(input("Введіть крок: "))

print(f"{'No':<5}{'x':<15}{'y':<20}")

i = 1
x = x_start

while True:   # імітація goto
    if x > x_end:
        break
    print(f"{i:<5}{x:<15.6f}{f(x):<20.6f}")
    x += step
    i += 1
