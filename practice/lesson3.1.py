"""Завдання 4"""
"""Рукасов Владислав"""

counter = 0
F = True 
G = False

while F and not G:
     counter += 1
     print("P: крок", counter)

     if counter == 3:
          G = True

     if not G:
          print("Q: додаткова дія")
     if counter >= 5:
          F = False