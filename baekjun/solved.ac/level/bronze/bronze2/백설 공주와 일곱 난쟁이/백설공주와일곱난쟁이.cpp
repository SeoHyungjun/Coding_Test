#include <iostream>
using namespace std;

int main() {
    int arr[9], idx = 0, sum = 0;
    
    for (auto &i : arr) {
        cin >> i;
        sum += i;
    }
    for (int i = 0; i < 8; i++) {
        for (int j = i+1; j < 9; j++) {
            if (sum - arr[i] - arr[j] != 100) continue;
            for (int k = 0; k < 9; k++) {
                if (k == i || k == j) continue;
                cout << arr[k] << '\n';
            }
        }
    }

    return 0;
}