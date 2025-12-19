from abc import ABC, abstractmethod
import math

#Практична робота №7 Рукасов 
#Абстрактний клас Трикутник
class Triangle(ABC):
    def __init__(self, side_a=1.0, side_b=1.0, angle=90.0):
        # приватні змінні (інкапсуляція)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__angle = angle

    # Геттери
    def get_sides(self):
        return self.__side_a, self.__side_b, self.__angle

    # Сеттери
    def set_sides(self, side_a, side_b, angle):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__angle = angle

    # Метод для виведення інформації
    def show_info(self):
        print(f"Сторони: a={self.__side_a}, b={self.__side_b}, кут={self.__angle}°")

    # Абстрактний метод обчислення площі
    @abstractmethod
    def area(self):
        pass


#Клас Прямокутний трикутник
class RightTriangle(Triangle):
    def __init__(self, side_a=1.0, side_b=1.0):
        # у прямокутному кут завжди 90°
        super().__init__(side_a, side_b, 90)

    def area(self):
        # Площа прямокутного трикутника
        a, b, _ = self.get_sides()
        return 0.5 * a * b

    def show_info(self):
        a, b, _ = self.get_sides()
        print(f"🔸 Прямокутний трикутник: a={a}, b={b}, площа={self.area():.2f}")


#Клас Рівнобедрений трикутник
class IsoscelesTriangle(Triangle):
    def __init__(self, side_a=1.0, side_b=1.0, angle=60.0):
        # сторона a = сторона b
        super().__init__(side_a, side_b, angle)

    def area(self):
        a, b, angle = self.get_sides()
        # Площа за формулою ½ab*sin(C)
        return 0.5 * a * b * math.sin(math.radians(angle))

    def show_info(self):
        a, b, angle = self.get_sides()
        print(f"🔹 Рівнобедрений трикутник: a={a}, b={b}, кут={angle}°, площа={self.area():.2f}")


#Функції для роботи зі списком трикутників
def find_triangle(triangles, triangle_type):
    """Пошук трикутників за типом"""
    result = [t for t in triangles if isinstance(t, triangle_type)]
    return result


def edit_triangle(triangle, new_a, new_b, new_angle=None):
    """Редагування параметрів трикутника"""
    if new_angle is None:
        new_angle = 90 if isinstance(triangle, RightTriangle) else 60
    triangle.set_sides(new_a, new_b, new_angle)


#Демонстрація роботи
if __name__ == "__main__":
    # створюємо декілька трикутників
    triangles = [
        RightTriangle(3, 4),
        IsoscelesTriangle(5, 5, 40),
        IsoscelesTriangle(6, 6, 60)
    ]

    print("📘 Список усіх трикутників:")
    for t in triangles:
        t.show_info()

    print("\n🔍 Пошук усіх рівнобедрених трикутників:")
    for t in find_triangle(triangles, IsoscelesTriangle):
        t.show_info()

    print("\n✏️ Редагування першого трикутника:")
    edit_triangle(triangles[0], 5, 12)
    triangles[0].show_info()
