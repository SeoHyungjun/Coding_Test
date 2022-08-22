#include <iostream>
#include <string>
using namespace std;

int main() {
    string user_input;

    while (true) {
        getline(cin, user_input, '\n');
        if (user_input == "END") break;

        for (int i = user_input.size()-1; i >= 0; i--) {
            cout << user_input[i];
        }
        cout << endl;
    }
    return 0;
}