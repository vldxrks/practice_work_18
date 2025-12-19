#include <iostream>
#include <cmath>
#include "root.h"

using namespace std;

int main() {
    double x(2.0);
    cout << "give your value for x: ";
    cin >> x;   // виправив << на >>
    
    cout << "sqrt(x) = " << sqrt(x) << endl;
    cout << "root(x) = " << root(x) << endl;

    return 0;
}
