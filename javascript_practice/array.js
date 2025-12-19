const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

/**
 * Фільтрує масив, залишаючи лише парні числа.
 * Умовою є: number % 2 === 0
 */
const evenNumbers = numbers.filter(function(number) {
  return number % 2 === 0;
});

// Або за допомогою стрілкової функції для більш короткого запису:
// const evenNumbers = numbers.filter(number => number % 2 === 0);

console.log(evenNumbers); // Виведе: [2, 4, 6, 8, 10]