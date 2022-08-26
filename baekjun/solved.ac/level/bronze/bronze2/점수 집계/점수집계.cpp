#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T, arr[5];
    cin >> T;
    for (int i = 0; i < T; i++) {
        for (int j = 0; j < 5; j++) cin >> arr[j];
        sort(arr, arr+5);

        if (arr[3] - arr[1] >= 4) cout << "KIN" << endl;
        else cout << arr[1] + arr[2] + arr[3] << endl;
    }

    return 0;
}