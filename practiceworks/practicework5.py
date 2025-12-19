#Практичне заняття №5 Рукасов Владислав 
# Програма: Протокол лижних гонок
filename = "SCI.txt"

# Кількість учасників
n = int(input("Введіть кількість учасників: "))

# Введення даних і запис у файл
with open(filename, "w", encoding="utf-8") as file:
    for i in range(n):
        print(f"\nУчасник №{i+1}")
        surname = input("Введіть прізвище: ")
        hour = int(input("Години: "))
        minute = int(input("Хвилини: "))
        second = int(input("Секунди: "))
        file.write(f"{surname} {hour} {minute} {second}\n")

print(f"\nДані успішно записано у файл '{filename}'.")

# Читання файлу і виведення тих, хто виконав норму (< 30 хвилин)
print("\nУчасники, які виконали норму (менше 30 хвилин):")
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split()
        surname = data[0]
        hour, minute, second = map(int, data[1:])

        total_seconds = hour * 3600 + minute * 60 + second
        if total_seconds < 30 * 60:  # менше 30 хвилин
            print(surname)
