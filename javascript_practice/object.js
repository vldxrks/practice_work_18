const user = {
  name: "Alex",
  age: 20,
  city: "Kyiv"
};

/**
 * Виводить інформацію про користувача у форматі: User [name] is [age] years old
 * @param {object} u - Об'єкт користувача.
 */
function displayUserInfo(u) {
  console.log(`User ${u.name} is ${u.age} years old`);
}

// Приклад використання:
displayUserInfo(user); // Виведе: User Alex is 20 years old