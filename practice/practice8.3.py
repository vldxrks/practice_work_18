import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return Complex(r, i)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        r = (self.real * other.real + self.imag * other.imag) / denom
        i = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(r, i)

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def power(self, n):
        r = math.hypot(self.real, self.imag)
        theta = math.atan2(self.imag, self.real)
        r_n = r ** n
        return Complex(r_n * math.cos(n * theta), r_n * math.sin(n * theta))

    def sqrt(self):
        r = math.hypot(self.real, self.imag)
        theta = math.atan2(self.imag, self.real) / 2
        return Complex(math.sqrt(r) * math.cos(theta), math.sqrt(r) * math.sin(theta))

    def __str__(self):
        return f"({self.real} {'+' if self.imag >= 0 else '-'} {abs(self.imag)}i)"

a = Complex(3, 4)
b = Complex(1, -2)

print("\nРобота з комплексними числами:")
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"Спряжене a: {a.conjugate()}")
print(f"a у 2 степені: {a.power(2)}")
print(f"√a = {a.sqrt()}")
