#include <iostream>
using namespace std;

string esPar(int a) {
    if(a % 2 == 0) {
        return "Es par";
    } else {
        return "Es impar";
    }
}

int main() {
    int a;

    cin >> a;

    cout << esPar(a) << endl;
    
    return 0;
}