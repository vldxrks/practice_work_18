#!/bin/bash
# countdown.sh: Зворотний відлік

echo "Введіть число для зворотного відліку:"
# Зчитування числа
read count

# Перевірка, чи введено додатне ціле число
if ! [[ "$count" =~ ^[0-9]+$ ]] || [ "$count" -lt 1 ]; then
  echo "Помилка: Будь ласка, введіть додатне ціле число."
  exit 1
fi

echo "--- Починаємо відлік від $count ---"

# Цикл while, доки значення count більше або дорівнює 1
while [ "$count" -ge 1 ]; do
  echo "$count"
  # Зменшення значення count на 1
  count=$((count - 1))
  sleep 0.5
done

echo "Старт!"