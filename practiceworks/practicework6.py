from datetime import date, timedelta

class MyDate:
    def __init__(self, year=2000, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
        self._validate_date()

    def _validate_date(self):
        """Перевірка правильності дати"""
        try:
            date(self.year, self.month, self.day)
        except ValueError:
            print("❌ Помилка: недопустима дата! Встановлено стандартне значення (2000-01-01).")
            self.year, self.month, self.day = 2000, 1, 1

    def input_date(self):
        """Ввід дати з клавіатури"""
        try:
            self.year = int(input("Введіть рік: "))
            self.month = int(input("Введіть місяць (1–12): "))
            self.day = int(input("Введіть день (1–31): "))
            self._validate_date()
        except ValueError:
            print("❌ Помилка вводу! Використовується дата за замовчуванням (2000-01-01).")
            self.year, self.month, self.day = 2000, 1, 1

    def display(self):
        """Вивід дати"""
        print(f"Дата: {self.year:04d}-{self.month:02d}-{self.day:02d}")

    def season(self):
        """Визначення пори року"""
        if self.month in (12, 1, 2):
            return "Зима"
        elif self.month in (3, 4, 5):
            return "Весна"
        elif self.month in (6, 7, 8):
            return "Літо"
        else:
            return "Осінь"

    def show_season(self):
        print(f"Пора року: {self.season()}")

    def to_date(self):
        """Перетворює на об’єкт datetime.date"""
        return date(self.year, self.month, self.day)

    def _safe_date(self, d: date):
        """Перевірка, щоб дата не вийшла за межі 1-9999 років"""
        if d.year < 1:
            return date(1, 1, 1)
        elif d.year > 9999:
            return date(9999, 12, 31)
        return d

    def __add__(self, other):
        """Перевантаження операції +"""
        if isinstance(other, MyDate):
            days_to_add = other.day + other.month * 30 + other.year * 365
            new_date = self.to_date() + timedelta(days=days_to_add)
        elif isinstance(other, int):
            new_date = self.to_date() + timedelta(days=other)
        else:
            raise TypeError("Невідомий тип для операції '+'")

        new_date = self._safe_date(new_date)
        return MyDate(new_date.year, new_date.month, new_date.day)

    def __sub__(self, other):
        """Перевантаження операції -"""
        if isinstance(other, MyDate):
            days_to_sub = other.day + other.month * 30 + other.year * 365
            new_date = self.to_date() - timedelta(days=days_to_sub)
        elif isinstance(other, int):
            new_date = self.to_date() - timedelta(days=other)
        else:
            raise TypeError("Невідомий тип для операції '-'")

        new_date = self._safe_date(new_date)
        return MyDate(new_date.year, new_date.month, new_date.day)


# === Демонстрація роботи програми ===
if __name__ == "__main__":
    print("=== Робота з класом MyDate ===\n")

    print("Введіть основну дату:")
    d1 = MyDate()
    d1.input_date()

    print("\nВаша дата:")
    d1.display()
    d1.show_season()

    print("\nВведіть другу дату (для додавання або віднімання):")
    d2 = MyDate()
    d2.input_date()

    print("\nРезультат додавання:")
    result_add = d1 + d2
    result_add.display()
    result_add.show_season()

    print("\nРезультат віднімання:")
    result_sub = d1 - d2
    result_sub.display()
    result_sub.show_season()
