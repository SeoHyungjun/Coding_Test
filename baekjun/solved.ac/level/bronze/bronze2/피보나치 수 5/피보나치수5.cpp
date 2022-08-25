#include <iostream>
using namespace std;

int main() {
    int N, arr[21];
    cin >> N;

    arr[0] = 0;
    arr[1] = 1;
    for (int i = 2; i < N+1; i++) arr[i] = arr[i-1] + arr[i-2];

    cout << arr[N];

    return 0;
}