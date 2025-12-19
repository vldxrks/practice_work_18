// 1) Сума чисел від 1 до N
let N = +prompt("Введіть N:");
let sum = 0;
for (let i = 1; i <= N; i++) {
  sum += i;
}
console.log("1) Сума чисел від 1 до", N, "=", sum);

// 2) Знайти найбільше число в масиві
let numbers = [12, 45, 3, 67, 21, 9];
let maxNum = numbers[0];
for (let num of numbers) {
  if (num > maxNum) maxNum = num;
}
console.log("2) Найбільше число в масиві =", maxNum);

// 3) Порахувати кількість парних чисел в масиві
let arr = [2, 7, 8, 11, 14, 20];
let evenCount = 0;
for (let i = 0; i < arr.length; i++) {
  if (arr[i] % 2 === 0) evenCount++;
}
console.log("3) Кількість парних чисел =", evenCount);

// 4) Вивести всі числа, більші за 10
let nums = [3, 11, 9, 15, 22, 5];
let greaterThan10 = [];
for (let n of nums) {
  if (n > 10) greaterThan10.push(n);
}
console.log("4) Числа більші за 10:", greaterThan10);

// 5) Множення елементів масиву на 5
let multArr = [1, 2, 3, 4, 5];
for (let i = 0; i < multArr.length; i++) {
  multArr[i] *= 5;
}
console.log("5) Множення елементів масиву на 5:", multArr);

// 6) Генерація масиву з 10 випадкових чисел (1–100) і вивести парні
let randomArr = [];
for (let i = 0; i < 10; i++) {
  randomArr.push(Math.floor(Math.random() * 100) + 1);
}
let evenNums = randomArr.filter(num => num % 2 === 0);
console.log("6) Випадковий масив:", randomArr);
console.log("   Парні числа:", evenNums);

// 7) Факторіал числа
let num = +prompt("Введіть число для факторіалу:");
let factorial = 1;
for (let i = 1; i <= num; i++) {
  factorial *= i;
}
console.log(`7) Факторіал числа ${num} = ${factorial}`);
