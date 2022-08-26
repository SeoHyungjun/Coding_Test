#include <iostream>
#include <string>
using namespace std;

int main() {
    int T, idx;
    string str;
    cin >> T;

    for (int i = 0; i < T; i++) {
        cin >> idx >> str;

        for (int j = 0; j < str.size(); j++) {
            if (j == idx - 1) continue;
            cout << str[j];
        }
        cout << endl;
    }

    return 0;
}