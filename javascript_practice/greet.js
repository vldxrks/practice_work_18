const userWithMethod = {
  name: "Olena",
  age: 25,
  /**
   * Виводить привітання з іменем користувача.
   */
  greet() {
    console.log(`Привіт! Мене звати ${this.name}.`);
  }
};

// Приклад використання:
userWithMethod.greet(); // Виведе: Привіт! Мене звати Olena.