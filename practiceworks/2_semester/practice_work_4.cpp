// =============================================================
// Лабораторна робота №4 — Бібліотека стандартних шаблонів (STL)
// Рукасов Владислав Ік-42
// =============================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <stdexcept>
#include <sstream>
#include <cassert>

using namespace std;

// =============================================================
// ЗАВДАННЯ 1
// Шаблонна функція створення, заповнення, сортування і виведення
// динамічного вектора
// =============================================================

template <typename T>
void vectorCreateFillSortPrint(int n, T startValue, T step)
{
    vector<T> v;

    // Заповнення вектора
    T val = startValue;
    for (int i = 0; i < n; i++) {
        v.push_back(val);
        val = val + step;
    }

    cout << "[Завд.1] Вектор до сортування: ";
    for (const T& el : v) cout << el << " ";
    cout << endl;

    // Сортування (за зростанням)
    sort(v.begin(), v.end());

    cout << "[Завд.1] Вектор після сортування: ";
    for (const T& el : v) cout << el << " ";
    cout << endl;
}

// =============================================================
// ЗАВДАННЯ 2
// Шаблонна функція читання текстового файлу та вставки елементів
// у список. T — тип елемента (int, double, string тощо)
// =============================================================

template <typename T>
list<T> fileToList(const string& filename)
{
    list<T> lst;
    ifstream fin(filename);
    if (!fin.is_open()) {
        cerr << "[Завд.2] Помилка: не вдалося відкрити файл '" << filename << "'\n";
        return lst;
    }
    T item;
    while (fin >> item) {
        lst.push_back(item);
    }
    fin.close();
    return lst;
}

template <typename T>
void printList(const list<T>& lst, const string& label = "")
{
    if (!label.empty()) cout << label << ": ";
    for (const T& el : lst) cout << el << " ";
    cout << endl;
}

// =============================================================
// ЗАВДАННЯ 3
// Програма: записує пари "номер місяця – назва місяця" в
// асоціативний масив (map) і за введеним номером друкує назву
// =============================================================

void task3_monthMap()
{
    map<int, string> months = {
        {1, "Січень"}, {2, "Лютий"},   {3, "Березень"},
        {4, "Квітень"},{5, "Травень"},  {6, "Червень"},
        {7, "Липень"}, {8, "Серпень"},  {9, "Вересень"},
        {10,"Жовтень"},{11,"Листопад"}, {12,"Грудень"}
    };

    cout << "[Завд.3] Введіть номер місяця (1-12): ";
    int num;
    cin >> num;

    auto it = months.find(num);
    if (it != months.end())
        cout << "[Завд.3] Місяць: " << it->second << endl;
    else
        cout << "[Завд.3] Невірний номер місяця!\n";
}

// =============================================================
// ЗАВДАННЯ 4
// Шаблонна функція послідовного пошуку значення в масиві
// Повертає вказівник на перший знайдений елемент або nullptr
// =============================================================

template <typename T>
const T* sequentialSearch(const T* arr, int size, const T& key)
{
    for (int i = 0; i < size; i++) {
        if (arr[i] == key)
            return &arr[i];
    }
    return nullptr;
}

void task4_demo()
{
    int arr[] = {5, 3, 8, 1, 9, 2, 7, 4, 6};
    int size = sizeof(arr) / sizeof(arr[0]);
    int key = 7;

    cout << "[Завд.4] Масив: ";
    for (int i = 0; i < size; i++) cout << arr[i] << " ";
    cout << "\n[Завд.4] Пошук ключа " << key << ": ";

    const int* found = sequentialSearch(arr, size, key);
    if (found)
        cout << "Знайдено! Значення: " << *found << endl;
    else
        cout << "Елемент не знайдено.\n";

    // Пошук відсутнього елемента
    key = 99;
    cout << "[Завд.4] Пошук ключа " << key << ": ";
    found = sequentialSearch(arr, size, key);
    if (found)
        cout << "Знайдено! Значення: " << *found << endl;
    else
        cout << "Елемент не знайдено.\n";
}

// =============================================================
// ЗАВДАННЯ 5
// Шаблонна функція сортування одновимірного масиву за зростанням
// методом бульбашки
// =============================================================

template <typename T>
void bubbleSort(T* arr, int size)
{
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - 1 - i; j++) {
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
        }
    }
}

void task5_demo()
{
    double arr[] = {3.5, 1.2, 4.8, 0.9, 2.3, 5.1};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "[Завд.5] До сортування:    ";
    for (int i = 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;

    bubbleSort(arr, size);

    cout << "[Завд.5] Після сортування: ";
    for (int i = 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;
}

// =============================================================
// ЗАВДАННЯ 6
// Функція-шаблон, яка перевіряє впорядкованість масиву
// Повертає: 1 - зростання, -1 - спадання, 0 - не впорядкований
// =============================================================

template <typename T>
int checkOrder(const T* arr, int size)
{
    if (size <= 1) return 1; // одноелементний масив — впорядкований

    bool ascending  = true;
    bool descending = true;

    for (int i = 0; i < size - 1; i++) {
        if (arr[i] > arr[i + 1]) ascending  = false;
        if (arr[i] < arr[i + 1]) descending = false;
    }

    if (ascending)  return  1;
    if (descending) return -1;
    return 0;
}

void task6_demo()
{
    int a1[] = {1, 2, 3, 4, 5};
    int a2[] = {5, 4, 3, 2, 1};
    int a3[] = {3, 1, 4, 1, 5};

    auto printOrder = [](int r) -> string {
        if (r ==  1) return "впорядкований за ЗРОСТАННЯМ";
        if (r == -1) return "впорядкований за СПАДАННЯМ";
        return "НЕ впорядкований";
    };

    cout << "[Завд.6] {1 2 3 4 5} -> " << printOrder(checkOrder(a1, 5)) << endl;
    cout << "[Завд.6] {5 4 3 2 1} -> " << printOrder(checkOrder(a2, 5)) << endl;
    cout << "[Завд.6] {3 1 4 1 5} -> " << printOrder(checkOrder(a3, 5)) << endl;
}

// =============================================================
// ЗАВДАННЯ 7
// Шаблонна функція формування файлу числових даних у текстовому
// форматі
// =============================================================

template <typename T>
bool writeNumericFile(const string& filename, const T* arr, int size)
{
    ofstream fout(filename);
    if (!fout.is_open()) {
        cerr << "[Завд.7] Помилка: не вдалося створити файл '" << filename << "'\n";
        return false;
    }
    for (int i = 0; i < size; i++) {
        fout << arr[i];
        if (i < size - 1) fout << "\n";
    }
    fout.close();
    cout << "[Завд.7] Файл '" << filename << "' записано (" << size << " елементів).\n";
    return true;
}

// =============================================================
// ЗАВДАННЯ 8
// Шаблонний клас КВАДРАТНА МАТРИЦЯ
// Обчислює контрольну суму як суму всіх елементів за модулем 2
// =============================================================

template <typename T>
class SquareMatrix {
    int n;
    vector<vector<T>> data;
public:
    explicit SquareMatrix(int size) : n(size), data(size, vector<T>(size, T())) {}

    // Заповнення
    void set(int i, int j, T val) { data[i][j] = val; }
    T    get(int i, int j) const  { return data[i][j]; }
    int  size() const             { return n; }

    // Виведення
    void print(const string& label = "Матриця") const {
        cout << label << ":\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                cout << data[i][j] << "\t";
            cout << "\n";
        }
    }

    // Контрольна сума (сума всіх елементів mod 2)
    long long checksum() const {
        long long sum = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                sum += static_cast<long long>(data[i][j]);
        return sum % 2;
    }
};

void task8_demo()
{
    SquareMatrix<int> m(3);
    int val = 1;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            m.set(i, j, val++);

    m.print("[Завд.8] Квадратна матриця 3x3");
    cout << "[Завд.8] Контрольна сума (sum mod 2) = " << m.checksum() << endl;
}

// =============================================================
// ЗАВДАННЯ 9
// Шаблонний клас СТЕК
// Параметризований рядками string; знаходить найдовший рядок
// =============================================================

template <typename T>
class MyStack {
    stack<T> st;
public:
    void push(const T& val) { st.push(val); }

    T pop() {
        if (st.empty()) throw runtime_error("Стек порожній!");
        T top = st.top();
        st.pop();
        return top;
    }

    T top() const {
        if (st.empty()) throw runtime_error("Стек порожній!");
        return st.top();
    }

    bool  empty() const { return st.empty(); }
    int   size()  const { return (int)st.size(); }

    // Пошук найдовшого рядка (для T = string)
    // Повертає найдовший елемент, не руйнуючи стек
    T findLongest() const {
        if (st.empty()) throw runtime_error("Стек порожній!");
        stack<T> tmp = st;
        T longest = tmp.top(); tmp.pop();
        while (!tmp.empty()) {
            T cur = tmp.top(); tmp.pop();
            if (cur.size() > longest.size()) longest = cur;
        }
        return longest;
    }
};

void task9_demo()
{
    MyStack<string> s;
    s.push("Hello");
    s.push("STL");
    s.push("StandardTemplateLibrary");
    s.push("C++");
    s.push("Programming");

    cout << "[Завд.9] Розмір стеку: " << s.size() << endl;
    cout << "[Завд.9] Найдовший рядок: \"" << s.findLongest() << "\"\n";

    cout << "[Завд.9] Вилучення зі стеку (LIFO): ";
    while (!s.empty()) cout << "\"" << s.pop() << "\" ";
    cout << endl;
}

// =============================================================
// ЗАВДАННЯ 10
// Шаблонний клас для роботи з однонаправленим лінійним списком
// Впорядкування за зростанням значень елементів
// =============================================================

template <typename T>
class SinglyLinkedList {
    struct Node {
        T data;
        Node* next;
        Node(const T& val) : data(val), next(nullptr) {}
    };
    Node* head;
    int   count;
public:
    SinglyLinkedList() : head(nullptr), count(0) {}

    ~SinglyLinkedList() { clear(); }

    void pushFront(const T& val) {
        Node* node = new Node(val);
        node->next = head;
        head = node;
        count++;
    }

    void pushBack(const T& val) {
        Node* node = new Node(val);
        if (!head) { head = node; }
        else {
            Node* cur = head;
            while (cur->next) cur = cur->next;
            cur->next = node;
        }
        count++;
    }

    void print(const string& label = "") const {
        if (!label.empty()) cout << label << ": ";
        Node* cur = head;
        while (cur) { cout << cur->data << " "; cur = cur->next; }
        cout << endl;
    }

    // Сортування вставками за зростанням
    void sortAscending() {
        if (!head || !head->next) return;
        // Збираємо елементи у вектор, сортуємо, відновлюємо
        vector<T> tmp;
        Node* cur = head;
        while (cur) { tmp.push_back(cur->data); cur = cur->next; }
        sort(tmp.begin(), tmp.end());
        cur = head;
        for (const T& v : tmp) { cur->data = v; cur = cur->next; }
    }

    void clear() {
        while (head) {
            Node* tmp = head->next;
            delete head;
            head = tmp;
        }
        count = 0;
    }

    int size() const { return count; }
};

void task10_demo()
{
    SinglyLinkedList<int> lst;
    lst.pushBack(5); lst.pushBack(2); lst.pushBack(8);
    lst.pushBack(1); lst.pushBack(9); lst.pushBack(3);

    lst.print("[Завд.10] Список до сортування");
    lst.sortAscending();
    lst.print("[Завд.10] Список після сортування");
}

// =============================================================
// ЗАВДАННЯ 11
// Шаблонний клас для роботи з лінійним списком з подвійними
// зв'язками. Занести елемент на початок; вилучити з кінця.
// =============================================================

template <typename T>
class DoublyLinkedList {
    struct Node {
        T data;
        Node* prev;
        Node* next;
        Node(const T& val) : data(val), prev(nullptr), next(nullptr) {}
    };
    Node* head;
    Node* tail;
    int   count;
public:
    DoublyLinkedList() : head(nullptr), tail(nullptr), count(0) {}

    ~DoublyLinkedList() { clear(); }

    // Додати на початок
    void pushFront(const T& val) {
        Node* node = new Node(val);
        if (!head) { head = tail = node; }
        else {
            node->next = head;
            head->prev = node;
            head = node;
        }
        count++;
    }

    // Додати в кінець
    void pushBack(const T& val) {
        Node* node = new Node(val);
        if (!tail) { head = tail = node; }
        else {
            node->prev = tail;
            tail->next = node;
            tail = node;
        }
        count++;
    }

    // Вилучити з кінця
    T popBack() {
        if (!tail) throw runtime_error("Список порожній!");
        T val = tail->data;
        Node* tmp = tail;
        if (tail == head) { head = tail = nullptr; }
        else {
            tail = tail->prev;
            tail->next = nullptr;
        }
        delete tmp;
        count--;
        return val;
    }

    // Вилучити з початку
    T popFront() {
        if (!head) throw runtime_error("Список порожній!");
        T val = head->data;
        Node* tmp = head;
        if (head == tail) { head = tail = nullptr; }
        else {
            head = head->next;
            head->prev = nullptr;
        }
        delete tmp;
        count--;
        return val;
    }

    void print(const string& label = "") const {
        if (!label.empty()) cout << label << ": ";
        Node* cur = head;
        while (cur) { cout << cur->data << " "; cur = cur->next; }
        cout << endl;
    }

    void clear() {
        while (head) {
            Node* tmp = head->next;
            delete head;
            head = tmp;
        }
        tail = nullptr;
        count = 0;
    }

    int size() const { return count; }
    bool empty() const { return count == 0; }
};

void task11_demo()
{
    DoublyLinkedList<int> lst;
    for (int i = 1; i <= 5; i++) lst.pushBack(i);

    lst.print("[Завд.11] Початковий список");

    lst.pushFront(0);
    lst.print("[Завд.11] Після pushFront(0)");

    int removed = lst.popBack();
    cout << "[Завд.11] Вилучено з кінця: " << removed << endl;
    lst.print("[Завд.11] Після popBack()");
}

// =============================================================
// ЗАВДАННЯ 12
// Шаблонний клас МНОЖИНА
// Операції: об'єднання (union_with), перетин (intersect),
// різниця (difference)
// =============================================================

template <typename T>
class MySet {
    set<T> data;
public:
    MySet() {}
    MySet(initializer_list<T> il) : data(il) {}

    void insert(const T& val) { data.insert(val); }
    bool contains(const T& val) const { return data.count(val) > 0; }
    int  size() const { return (int)data.size(); }

    void print(const string& label = "") const {
        if (!label.empty()) cout << label << ": { ";
        else cout << "{ ";
        for (const T& v : data) cout << v << " ";
        cout << "}\n";
    }

    // Об'єднання A ∪ B
    MySet<T> union_with(const MySet<T>& other) const {
        MySet<T> result;
        for (const T& v : data)       result.insert(v);
        for (const T& v : other.data) result.insert(v);
        return result;
    }

    // Перетин A ∩ B
    MySet<T> intersect(const MySet<T>& other) const {
        MySet<T> result;
        for (const T& v : data)
            if (other.contains(v)) result.insert(v);
        return result;
    }

    // Різниця A \ B
    MySet<T> difference(const MySet<T>& other) const {
        MySet<T> result;
        for (const T& v : data)
            if (!other.contains(v)) result.insert(v);
        return result;
    }
};

void task12_demo()
{
    MySet<int> A = {1, 2, 3, 4, 5};
    MySet<int> B = {3, 4, 5, 6, 7};

    A.print("[Завд.12] A");
    B.print("[Завд.12] B");
    A.union_with(B).print("[Завд.12] A ∪ B");
    A.intersect(B).print("[Завд.12] A ∩ B");
    A.difference(B).print("[Завд.12] A \\ B");
    B.difference(A).print("[Завд.12] B \\ A");
}

// =============================================================
// ЗАВДАННЯ 13
// Шаблонний клас ЧЕРГА З ПРІОРИТЕТАМИ
// Занести елемент; вилучити елемент з найвищим і найнижчим
// пріоритетами
// =============================================================

template <typename T>
class PriorityQueue {
    // maxHeap — для найвищого пріоритету (більше значення = вищий пріоритет)
    priority_queue<T>                         maxHeap;
    // minHeap — для найнижчого пріоритету
    priority_queue<T, vector<T>, greater<T>>  minHeap;

    // Синхронізуємо обидві структури
    vector<T> storage; // зберігаємо всі елементи для перебудови

    void rebuild() {
        while (!maxHeap.empty()) maxHeap.pop();
        while (!minHeap.empty()) minHeap.pop();
        for (const T& v : storage) {
            maxHeap.push(v);
            minHeap.push(v);
        }
    }

    void removeFromStorage(const T& val) {
        auto it = find(storage.begin(), storage.end(), val);
        if (it != storage.end()) storage.erase(it);
    }

public:
    void push(const T& val) {
        storage.push_back(val);
        maxHeap.push(val);
        minHeap.push(val);
        cout << "[Завд.13] Додано до черги: " << val << endl;
    }

    // Вилучити елемент з НАЙВИЩИМ пріоритетом
    T popMax() {
        if (maxHeap.empty()) throw runtime_error("Черга порожня!");
        T val = maxHeap.top();
        maxHeap.pop();
        removeFromStorage(val);
        rebuild();
        return val;
    }

    // Вилучити елемент з НАЙНИЖЧИМ пріоритетом
    T popMin() {
        if (minHeap.empty()) throw runtime_error("Черга порожня!");
        T val = minHeap.top();
        minHeap.pop();
        removeFromStorage(val);
        rebuild();
        return val;
    }

    T peekMax() const {
        if (maxHeap.empty()) throw runtime_error("Черга порожня!");
        return maxHeap.top();
    }

    T peekMin() const {
        if (minHeap.empty()) throw runtime_error("Черга порожня!");
        return minHeap.top();
    }

    bool empty() const { return storage.empty(); }
    int  size()  const { return (int)storage.size(); }

    void print(const string& label = "") const {
        if (!label.empty()) cout << label << ": ";
        vector<T> tmp = storage;
        sort(tmp.begin(), tmp.end(), greater<T>());
        cout << "[ ";
        for (const T& v : tmp) cout << v << " ";
        cout << "]\n";
    }
};

void task13_demo()
{
    PriorityQueue<int> pq;
    pq.push(10);
    pq.push(3);
    pq.push(7);
    pq.push(1);
    pq.push(15);
    pq.push(6);

    pq.print("[Завд.13] Черга (відсортована за спаданням)");

    cout << "[Завд.13] Найвищий пріоритет (peek): " << pq.peekMax() << endl;
    cout << "[Завд.13] Найнижчий пріоритет (peek): " << pq.peekMin() << endl;

    int maxEl = pq.popMax();
    cout << "[Завд.13] Вилучено MAX: " << maxEl << endl;
    pq.print("[Завд.13] Черга після popMax");

    int minEl = pq.popMin();
    cout << "[Завд.13] Вилучено MIN: " << minEl << endl;
    pq.print("[Завд.13] Черга після popMin");
}

// =============================================================
// MAIN — демонстрація всіх завдань
// =============================================================

int main()
{
    cout << "============================================\n";
    cout << " ЗАВДАННЯ 1: Вектор (int)\n";
    cout << "============================================\n";
    // Заповнюємо вектор з 8 цілих чисел у зворотньому порядку
    int arr1[] = {9, 3, 7, 1, 5, 8, 2, 6};
    vector<int> v1(arr1, arr1 + 8);
    cout << "[Завд.1] Вектор до сортування:    ";
    for (int x : v1) cout << x << " ";
    cout << "\n";
    sort(v1.begin(), v1.end());
    cout << "[Завд.1] Вектор після сортування: ";
    for (int x : v1) cout << x << " ";
    cout << "\n";
    // Також через шаблонну функцію з double
    vectorCreateFillSortPrint<double>(6, 6.0, -1.5);

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 2: Файл -> список\n";
    cout << "============================================\n";
    // Створюємо тестовий файл
    {
        ofstream tmp("task2_data.txt");
        tmp << "42\n17\n5\n99\n3\n78\n";
    }
    list<int> lst2 = fileToList<int>("task2_data.txt");
    printList(lst2, "[Завд.2] Список зі файлу");

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 3: Місяці\n";
    cout << "============================================\n";
    {
        map<int, string> months = {
            {1,"Січень"},{2,"Лютий"},{3,"Березень"},{4,"Квітень"},
            {5,"Травень"},{6,"Червень"},{7,"Липень"},{8,"Серпень"},
            {9,"Вересень"},{10,"Жовтень"},{11,"Листопад"},{12,"Грудень"}
        };
        // Демонстрація без введення: виводимо кілька прикладів
        for (int num : {3, 7, 12}) {
            auto it = months.find(num);
            cout << "[Завд.3] Місяць №" << num << " -> " << it->second << endl;
        }
    }

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 4: Послідовний пошук\n";
    cout << "============================================\n";
    task4_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 5: Сортування бульбашкою\n";
    cout << "============================================\n";
    task5_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 6: Перевірка впорядкованості\n";
    cout << "============================================\n";
    task6_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 7: Формування файлу числових даних\n";
    cout << "============================================\n";
    {
        double data7[] = {1.1, 2.2, 3.3, 4.4, 5.5};
        writeNumericFile<double>("task7_output.txt", data7, 5);
        // Верифікуємо — зчитуємо назад
        ifstream f7("task7_output.txt");
        cout << "[Завд.7] Зчитано назад: ";
        double x;
        while (f7 >> x) cout << x << " ";
        cout << endl;
    }

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 8: Квадратна матриця\n";
    cout << "============================================\n";
    task8_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 9: Стек рядків\n";
    cout << "============================================\n";
    task9_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 10: Однонаправлений список\n";
    cout << "============================================\n";
    task10_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 11: Двонаправлений список\n";
    cout << "============================================\n";
    task11_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 12: Множина\n";
    cout << "============================================\n";
    task12_demo();

    cout << "\n============================================\n";
    cout << " ЗАВДАННЯ 13: Черга з пріоритетами\n";
    cout << "============================================\n";
    task13_demo();

    return 0;
}