#include <iostream>
using namespace std;

//Перевантаження за типом аргументів
void showInfo(int a) {
    cout << "Ціле число: " << a << ", його квадрат = " << a * a << endl;
}

void showInfo(double a) {
    cout << "Дійсне число: " << a << ", його куб = " << a * a * a << endl;
}

//Перевантаження за кількістю аргументів     
int add(int a, int b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}

int main() {
    cout << "=== Перевантаження за типом аргументів ===" << endl;
    showInfo(5);        // викличе варіант з int
    showInfo(2.5);      // викличе варіант з double

    cout << "\n=== Перевантаження за кількістю аргументів ===" << endl;
    cout << "Сума двох чисел: " << add(3, 7) << endl;      // викличе add(int, int)
    cout << "Сума трьох чисел: " << add(1, 2, 3) << endl;  // викличе add(int, int, int)

    return 0;
}
