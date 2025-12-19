/**
 * Виконує операцію (callback) над двома числами.
 * @param {number} a - Перше число.
 * @param {number} b - Друге число.
 * @param {function} operation - Функція, яка приймає (a, b) і повертає результат.
 * @returns {number} Результат операції.
 */
function calc(a, b, operation) {
  return operation(a, b);
}

// Визначення callback-функцій:
const add = (x, y) => x + y;
const multiply = (x, y) => x * y;

// Приклади використання:
console.log("Додавання: ", calc(10, 5, add));     // Виведе: Додавання: 15
console.log("Множення: ", calc(10, 5, multiply)); // Виведе: Множення: 50
console.log("Віднімання: ", calc(10, 5, (x, y) => x - y)); // Виведе: Віднімання: 5