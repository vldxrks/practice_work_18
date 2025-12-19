// class Employee (використовує void info())
#include <iostream>
#include <string>
#include <vector>

class Employee {
private:
    std::string name;
public:
    Employee(const std::string& n) : name(n) {}
    ~Employee() {}
    void info() const {
        std::cout << "Працівник: " << name;
    }
}; 

class Employer {
private:
    size_t size;
    std::vector<Employee*> places;
public:
    Employer(size_t sz) : size(sz), places(sz, nullptr) {}
    ~Employer() {
        for (auto e : places) {
            delete e;
        }
    }
    void hire(Employee* e) {
        for (size_t i = 0; i < size; i++) {
            if (places[i] == nullptr) {
                places[i] = e;
                std::cout << "Працівника ";
                e->info();
                std::cout << " найнято на місце #" << i << "\n";
                return;
            }
        }
        std::cout << "Немає жодного вакантного робочого місця! Працівник ";
        e->info();
        std::cout << " не найнятий.\n";
        delete e;
    }
    void show() const {
        std::cout << "\nСтан робочих місць:\n";
        for (size_t i = 0; i < size; i++) {
            std::cout << "Місце #" << i << ": ";
            if (places[i] == nullptr)
                std::cout << "вільне\n";
            else {
                places[i]->info();
                std::cout << "\n";
            }
        }
    }
};

int main() {
    Employer company(3);
    company.hire(new Employee("Іван"));
    company.hire(new Employee("Олена"));
    company.hire(new Employee("Петро"));
    company.hire(new Employee("Марія")); // має не найнятись
    company.show();
    return 0;
}