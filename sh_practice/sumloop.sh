#!/bin/bash
# sumloop.sh: Обчислення суми чисел від 1 до 10

SUM=0
START=1
END=10

echo "Обчислення суми чисел від $START до $END..."

# Цикл перебирає числа від 1 до 10
for i in $(seq $START $END); do
  # Додавання поточного числа до загальної суми
  SUM=$((SUM + i))
done

echo "Загальна сума чисел від $START до $END дорівнює: $SUM"