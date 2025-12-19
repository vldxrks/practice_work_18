#include <iostream>
#include <vector>
#include <string>

// --- Базовий клас ---
class University {
protected:
    std::string name;
public:
    University(std::string n) : name(n) {}
    
    // Віртуальна функція дозволяє викликати метод похідного класу через указівник на базовий
    virtual void showInfo() {
        std::cout << "[Університет] Назва: " << name << std::endl;
    }
    
    // Віртуальний деструктор важливий для правильного очищення пам'яті
    virtual ~University() {}
};

// --- Похідний клас 1 рівня ---
class Faculty : public University {
protected:
    std::string facultyName;
public:
    Faculty(std::string uN, std::string fN) : University(uN), facultyName(fN) {}
    
    void showInfo() override {
        std::cout << "[Факультет] Університет: " << name 
                  << " | Факультет: " << facultyName << std::endl;
    }
};

// --- Похідний клас 2 рівня ---
class Department : public Faculty {
    std::string deptName;
public:
    Department(std::string uN, std::string fN, std::string dN) 
        : Faculty(uN, fN), deptName(dN) {}
    
    void showInfo() override {
        std::cout << "[Кафедра] Університет: " << name 
                  << " | Факультет: " << facultyName 
                  << " | Кафедра: " << deptName << std::endl;
    }
};

// --- ГОЛОВНА ФУНКЦІЯ ---
int main() {
    // Встановлюємо кодування для виводу кирилиці (якщо потрібно)
    // system("chcp 1251"); 

    // Створюємо масив указівників на базовий тип
    University* list[3];

    // Заповнюємо об'єктами різних типів (Upcasting)
    list[0] = new University("Київський Політехнічний Інститут");
    list[1] = new Faculty("Львівська Політехніка", "ІКТА");
    list[2] = new Department("КНУ ім. Шевченка", "Кібернетика", "ММСА");

    std::cout << "--- Вивід даних через масив указівників ---" << std::endl;

    // Вивід у циклі
    for(int i = 0; i < 3; i++) {
        list[i]->showInfo();
    }

    // Очищення динамічної пам'яті
    for(int i = 0; i < 3; i++) {
        delete list[i];
    }

    return 0;
}