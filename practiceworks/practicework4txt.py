# Зчитування даних із файлу students.txt
filename = r"C:\Users\vladr\Documents\classworks\practiceworks\students.txt"

students = []

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 5:  # Прізвище_Ініціали + 4 оцінки
            name = parts[0].replace("_", " ")  # Повертаємо пробіли
            marks = list(map(int, parts[1:]))
            avg = sum(marks) / len(marks)
            students.append([name, *marks, avg])

# Виведення таблиці студентів із середнім балом < 4
print("Студенти із середнім балом менше 4:\n")
print(f"{'№':<3} {'Прізвище та ініціали':<20} {'Інф.':<5} {'Вища мат.':<10} {'Фізика':<8} {'Програм.':<10} {'Сер. бал':<8}")
print("-" * 75)

for i, s in enumerate(students, start=1):
    if s[5] < 4:
        print(f"{i:<3} {s[0]:<20} {s[1]:<5} {s[2]:<10} {s[3]:<8} {s[4]:<10} {s[5]:<8.2f}")
