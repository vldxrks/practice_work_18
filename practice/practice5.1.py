import random

# Блок Б. Двовимірний масив 3x3
rows, cols = 3, 3
matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]

print("\nДвовимірний масив (матриця 3x3):")
for row in matrix:
    print(row)
