#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
    
    int K;
    cin >> K;
    for (int i = 0; i < K; i++) {
        int N, arr[50] = {0, };
        cin >> N;
        for (int j = 0; j < N; j++) {
            cin >> arr[j];
        }
        sort(arr, arr+N, greater<int>());

        int max_point = arr[0], min_point = arr[N-1];
        int max_gap = 0;

        for (int j = 0; j < N-1; j++) {
            max_gap = max(max_gap, arr[j] - arr[j+1]);
        }

        cout << "Class " << i+1 << "\n";
        cout << "Max " << max_point << ", Min " << min_point << ", Largest gap " << max_gap << '\n';
    }

    return 0;
}