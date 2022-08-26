#include <iostream>
using namespace std;

int main() {
    int t, n;

    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;

        int left = 100, right = -1, cur;
        for (int j = 0; j < n; j++) {
            cin >> cur;
            left = min(left, cur);
            right = max(right, cur);
        }

        cout << (right - left) * 2 << endl;
    }

    return 0;
}