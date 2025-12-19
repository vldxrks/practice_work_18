#!/bin/bash
# waitfile.sh: Очікування файлу result.txt

FILE_TO_WAIT="result.txt"
echo "Очікування появи файлу: $FILE_TO_WAIT"

# Цикл until продовжує виконуватися, доки умова НЕ є істинною
# [ -f "$FILE_TO_WAIT" ] перевіряє, чи існує файл і чи є він звичайним файлом
until [ -f "$FILE_TO_WAIT" ]; do
  echo "Файл $FILE_TO_WAIT ще не знайдено. Чекаю..."
  # Пауза на 1 секунду
  sleep 1
done

echo "Файл знайдено: $FILE_TO_WAIT"