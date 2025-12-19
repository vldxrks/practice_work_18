class Student:
    def __init__(self, surname, initials, group, grades):
        self.surname = surname
        self.initials = initials
        self.group = group
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def is_good_student(self):
        return all(grade >= 4 for grade in self.grades)

students = [
    Student("Іваненко", "І.І.", "КН-101", [5, 4, 5, 5, 4]),
    Student("Петренко", "П.П.", "КН-101", [3, 4, 3, 4, 4]),
    Student("Сидоренко", "С.С.", "КН-102", [4, 4, 5, 5, 5]),
    Student("Мельник", "М.М.", "КН-103", [2, 3, 4, 3, 2])
]

# Сортування за середнім балом
students.sort(key=lambda s: s.average())

print("\nСтуденти за зростанням середнього балу:")
for s in students:
    print(f"{s.surname} {s.initials} ({s.group}) - середній бал: {s.average():.2f}")

print("\nСтуденти, що мають лише 4 або 5:")
for s in students:
    if s.is_good_student():
        print(f"{s.surname} ({s.group})")
