def sum_of_divisors(n):
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

def friendly_numbers(a, b):
    pairs = []
    for x in range(a, b + 1):
        y = sum_of_divisors(x)
        if y > x and y <= b and sum_of_divisors(y) == x:
            pairs.append((x, y))
    return pairs

a, b = 1, 10000
print("Дружні числа на відрізку [1; 10000]:")
for pair in friendly_numbers(a, b):
    print(pair)
