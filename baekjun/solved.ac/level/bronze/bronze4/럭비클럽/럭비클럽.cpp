#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    int age = 0, weight = 0;

    while (1) {
        cin >> name >> age >> weight;
        if (name == "#" && age == 0 && weight == 0) break;
        
        cout << name << " ";
        if (age > 17 || weight >= 80) {
            cout << "Senior" << endl;
        } else {
            cout << "Junior" << endl;
        }
    }
    return 0;
}