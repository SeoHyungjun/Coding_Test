#include <iostream>
using namespace std;

int main() {
    int total, cur;
    cin >> total;
    for (int i = 0; i < 9; i++) {
        cin >> cur;
        total -= cur;
    }
    cout << total;

    return 0;
}