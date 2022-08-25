#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    int N, A[1000001], B, C, cur;
    long long answer = 0;

    cin >> N;
    for (int i = 0; i < N; i++) cin >> A[i];
    cin >> B >> C;

    for (int i = 0; i < N; i++) {
        if (A[i] <= B) answer += 1;
        else if ((A[i] - B) % C == 0) answer += (A[i] - B) / C + 1;
        else answer += (A[i] - B) / C + 2;
    }

    cout << answer;

    return 0;
}