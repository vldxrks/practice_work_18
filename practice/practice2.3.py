import math

def calculate_z(x):
    """
    Обчислює значення функції z в залежності від x.
    """
    if 0 <= x <= 0.3:
        # Перша частина функції
        return x**3 + math.sin(x)
    elif 0.3 < x <= 2:
        # Друга частина функції
        # Важливо: перевірка x > 0 для ln(x)
        if x > 0:
            return math.atan(x + math.log(x))
        else:
            return float('nan') # Повертаємо "не число" якщо x <= 0, щоб уникнути помилки
    else:
        return float('nan') # Повертаємо "не число" для значень поза діапазоном [0, 2]

# Введення даних від користувача
try:
    start_x = float(input("Введіть початкове значення аргументу (наприклад, 0): "))
    end_x = float(input("Введіть кінцеве значення аргументу (наприклад, 2): "))
    step_x = float(input("Введіть крок зміни аргументу (наприклад, 0.3): "))
except ValueError:
    print("Помилка: Введено некоректні дані. Будь ласка, введіть числові значення.")
    exit()

# Заголовок таблиці
print("-" * 40)
print(f"{'No точки':<10} | {'Значення x':<15} | {'Значення z':<15}")
print("-" * 40)

# Цикл обчислень і виведення
point_number = 1
current_x = start_x

while current_x <= end_x:
    z_value = calculate_z(current_x)

    # Перевірка на "не число"
    if not math.isnan(z_value):
        print(f"{point_number:<10} | {current_x:<15.4f} | {z_value:<15.4f}")
    
    current_x += step_x
    point_number += 1

print("-" * 40)