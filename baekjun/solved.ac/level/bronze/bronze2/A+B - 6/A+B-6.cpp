#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    string N;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        cout << N[0] - '0' + N[2] - '0' << endl;
    }

    return 0;
}