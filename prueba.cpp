#include <iostream>
using namespace std;

int suma(int a, int b) {
    return a + b;
}

int main() {
    int a, b;

    cin >> a >> b;

    cout << "La suma es " << suma(a, b) << endl;
    
    return 0;
}