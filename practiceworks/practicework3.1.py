#Практична робота №3 Рукасов Владислав 
#Завдання №2 10 варіант
import math

# Ввід розмірів матриці
m = int(input("Введіть кількість координат у векторі (m ≤ 5): "))
n = int(input("Введіть кількість векторів (n ≤ 6): "))

# Ввід матриці A(m, n)
A = []
print("Введіть координати векторів:")
for i in range(n):
    vector = []
    for j in range(m):
        x = float(input(f"A[{j+1},{i+1}] = "))
        vector.append(x)
    A.append(vector)

# Обчислення довжин векторів
lengths = []
for vector in A:
    length = math.sqrt(sum([x**2 for x in vector]))
    lengths.append(length)

# Виведення довжин
print("\nДовжини векторів:")
for i, l in enumerate(lengths, start=1):
    print(f"Вектор {i}: довжина = {l:.3f}")

# Знаходження максимального елемента та його індексу
max_value = max(lengths)
max_index = lengths.index(max_value) + 1

print(f"\nМаксимальна довжина = {max_value:.3f}, номер вектора = {max_index}")
