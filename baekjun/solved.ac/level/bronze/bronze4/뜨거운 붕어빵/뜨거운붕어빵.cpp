#include <iostream>
#include <string>
using namespace std;

int main() {
    int N = 0, M = 0;
    string cur;

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        cin >> cur;
        for (int j = cur.size() - 1; j >= 0; j--) cout << cur[j];
        cout << endl;
    }
    return 0;
}