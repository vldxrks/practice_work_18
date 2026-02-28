import math
from abc import ABC, abstractmethod

print("=== ЛАБОРАТОРНА РОБОТА: ПОЛІМОРФІЗМ У PYTHON ===")
# Рукасов Владислав Ік-42
# ==========================================
# ЗАВДАННЯ 1: Площі фігур [cite: 534, 535]
# ==========================================
class ShapeBase(ABC):
    @abstractmethod
    def area(self): pass

class Rect(ShapeBase):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Circ(ShapeBase):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * (self.r ** 2)

def run_task_1():
    print("\n--- Завдання 1: Площі фігур ---")
    shapes = [Rect(4, 5), Circ(3)]
    for s in shapes:
        print(f"Площа {s.__class__.__name__}: {s.area():.2f}")

# ==========================================
# ЗАВДАННЯ 2: Норма (Комплексні, Вектор, Матриця) [cite: 536, 537, 538, 539]
# ==========================================
class MathObject(ABC):
    @abstractmethod
    def norma(self): pass

class ComplexNum(MathObject):
    def __init__(self, real, imag): self.real, self.imag = real, imag
    def norma(self): return math.sqrt(self.real**2 + self.imag**2)

class Vector(MathObject):
    def __init__(self, coords): self.coords = coords
    def norma(self): return math.sqrt(sum(x**2 for x in self.coords))

class Matrix(MathObject):
    def __init__(self, mat): self.mat = mat
    def norma(self): return max(abs(val) for row in self.mat for val in row)

def run_task_2():
    print("\n--- Завдання 2: Норма ---")
    objects = [ComplexNum(3, 4), Vector([1, 2, 2]), Matrix([[1, -9], [4, 5]])]
    for obj in objects:
        print(f"Норма {obj.__class__.__name__}: {obj.norma():.2f}")

# ==========================================
# ЗАВДАННЯ 3: Криві y(x) [cite: 540, 541, 542, 543]
# ==========================================
class Curve(ABC):
    @abstractmethod
    def calculate_y(self, x): pass

class Line(Curve):
    def __init__(self, a, b): self.a, self.b = a, b
    def calculate_y(self, x): return self.a * x + self.b

class Ellipse(Curve):
    def __init__(self, a, b): self.a, self.b = a, b
    def calculate_y(self, x):
        if abs(x) > self.a: return None # Поза межами еліпса
        return self.b * math.sqrt(1 - (x**2)/(self.a**2))

def run_task_3():
    print("\n--- Завдання 3: Криві ---")
    curves = [Line(2, 3), Ellipse(5, 3)]
    x = 4
    for c in curves:
        print(f"y({x}) для {c.__class__.__name__}: {c.calculate_y(x)}")

# ==========================================
# ЗАВДАННЯ 4: Прогресії [cite: 544, 545, 546, 547, 548]
# ==========================================
class Progression(ABC):
    def __init__(self, a0, step):
        self.a0 = a0
        self.step = step # різниця або відношення
        
    @abstractmethod
    def sum_progression(self, n): pass

class Arithmetic(Progression):
    def sum_progression(self, n):
        an = self.a0 + (n - 1) * self.step
        return n * (self.a0 + an) / 2

class Geometric(Progression):
    def sum_progression(self, n):
        if self.step == 1: return self.a0 * n
        an = self.a0 * (self.step ** (n - 1))
        return (self.a0 - an * self.step) / (1 - self.step)

def run_task_4():
    print("\n--- Завдання 4: Прогресії ---")
    progs = [Arithmetic(1, 2), Geometric(2, 3)] # n=5 для обох
    for p in progs:
        print(f"Сума 5 елементів {p.__class__.__name__}: {p.sum_progression(5)}")

# ==========================================
# ЗАВДАННЯ 5: Стек і Черга на базі Списку [cite: 549, 550, 551]
# ==========================================
class BaseList(ABC):
    def __init__(self): self.data = []
    @abstractmethod
    def push(self, item): pass
    @abstractmethod
    def pop(self): pass

class Stack(BaseList):
    def push(self, item): self.data.append(item)
    def pop(self): return self.data.pop() if self.data else None

class Queue(BaseList):
    def push(self, item): self.data.append(item)
    def pop(self): return self.data.pop(0) if self.data else None

def run_task_5():
    print("\n--- Завдання 5: Стек і Черга ---")
    collections = [Stack(), Queue()]
    for c in collections:
        c.push(1); c.push(2); c.push(3)
        print(f"{c.__class__.__name__} pop: {c.pop()}") # Stack->3, Queue->1

# ==========================================
# ЗАВДАННЯ 6: Геометричні Фігури (Периметр і Площа) [cite: 552, 554, 555, 556, 557, 558]
# ==========================================
class GeoFigure(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
    def print_info(self):
        print(f"{self.__class__.__name__}: Площа = {self.area():.2f}, Периметр = {self.perimeter():.2f}")

class CircleFull(GeoFigure):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r**2
    def perimeter(self): return 2 * math.pi * self.r

def run_task_6():
    print("\n--- Завдання 6: Фігури детально ---")
    figs = [CircleFull(5)] # Можна додати прямокутник і трапецію аналогічно
    for f in figs: f.print_info()

# ==========================================
# ЗАВДАННЯ 7: Працівники та зарплата [cite: 559, 560, 561]
# ==========================================
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self): pass

class HourlyWorker(Employee):
    def __init__(self, rate, hours): self.rate, self.hours = rate, hours
    def calculate_salary(self): return self.rate * self.hours

class SalariedWorker(Employee):
    def __init__(self, salary): self.salary = salary
    def calculate_salary(self): return self.salary

def run_task_7():
    print("\n--- Завдання 7: Зарплата ---")
    workers = [HourlyWorker(150, 40), SalariedWorker(20000)]
    for w in workers: print(f"{w.__class__.__name__}: {w.calculate_salary()} грн")

# ==========================================
# ЗАВДАННЯ 8: 3D Фігури [cite: 562, 563, 564, 565, 566]
# ==========================================
class Shape3D(ABC):
    @abstractmethod
    def surface_area(self): pass

class Sphere(Shape3D):
    def __init__(self, r): self.r = r
    def surface_area(self): return 4 * math.pi * self.r**2

class Tetrahedron(Shape3D):
    def __init__(self, a): self.a = a
    def surface_area(self): return (self.a**2) * math.sqrt(3)

def run_task_8():
    print("\n--- Завдання 8: Площа поверхні 3D ---")
    shapes = [Sphere(4), Tetrahedron(5)]
    for s in shapes: print(f"Поверхня {s.__class__.__name__}: {s.surface_area():.2f}")

# ==========================================
# ЗАВДАННЯ 9: Ссавці [cite: 567, 568, 569]
# ==========================================
class Mammal(ABC):
    @abstractmethod
    def describe(self): pass

class Human(Mammal):
    def describe(self): return "Людина: двоногий ссавець, мислить."

class Animal(Mammal): pass

class Horse(Animal):
    def describe(self): return "Кінь: копитна тварина, використовується для їзди."

def run_task_9():
    print("\n--- Завдання 9: Ссавці ---")
    mammals = [Human(), Horse()]
    for m in mammals: print(m.describe())

# ==========================================
# ЗАВДАННЯ 10: Батько і Дитина [cite: 570, 571, 572, 573]
# ==========================================
class Father:
    def __init__(self, name): self.name = name
    def print_name(self): print(f"Ім'я: {self.name}")

class Child(Father):
    def __init__(self, name, father_name):
        super().__init__(name)
        self.patronymic = father_name + "ович/на"
        
    def print_name(self): print(f"Ім'я дитини: {self.name}, По батькові: {self.patronymic}")

def run_task_10():
    print("\n--- Завдання 10: Батько і Дитина ---")
    people = [Father("Іван"), Child("Олексій", "Іван")]
    for p in people: p.print_name()

# ==========================================
# ЗАВДАННЯ 12: Корені рівнянь [cite: 574, 575, 576]
# ==========================================
class Equation(ABC):
    @abstractmethod
    def roots(self): pass

class Linear(Equation):
    def __init__(self, a, b): self.a, self.b = a, b
    def roots(self): return [-self.b / self.a] if self.a != 0 else []

class Quadratic(Equation):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def roots(self):
        d = self.b**2 - 4*self.a*self.c
        if d < 0: return []
        if d == 0: return [-self.b / (2*self.a)]
        return [(-self.b - math.sqrt(d))/(2*self.a), (-self.b + math.sqrt(d))/(2*self.a)]

def run_task_12():
    print("\n--- Завдання 12: Корені рівнянь ---")
    eqs = [Linear(2, -4), Quadratic(1, -3, 2)]
    for e in eqs: print(f"Корені рівняння {e.__class__.__name__}: {e.roots()}")

# ==========================================
# ЗАВДАННЯ 13: Фігури на екрані [cite: 577, 578, 579, 580, 581, 582]
# ==========================================
class ScreenFigure(ABC):
    def __init__(self, x, y):
        self._x, self._y = x, y
        self._angle, self._scale = 0, 1.0

    def move(self, dx, dy): self._x += dx; self._y += dy
    def rotate(self, deg): self._angle += deg
    
    @abstractmethod
    def draw(self): pass

class ScreenTriangle(ScreenFigure):
    def draw(self): print(f"Малюємо Трикутник в ({self._x}, {self._y}), кут {self._angle}")

def run_task_13():
    print("\n--- Завдання 13: Фігури на екрані ---")
    figures = [ScreenTriangle(10, 20)]
    for f in figures:
        f.rotate(45); f.move(5, 5)
        f.draw()

# ==========================================
# ГОЛОВНИЙ БЛОК: Виклик усіх завдань
# ==========================================
if __name__ == "__main__":
    run_task_1()
    run_task_2()
    run_task_3()
    run_task_4()
    run_task_5()
    run_task_6()
    run_task_7()
    run_task_8()
    run_task_9()
    run_task_10()
    run_task_12()
    run_task_13()