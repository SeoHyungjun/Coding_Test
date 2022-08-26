#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

    int K, P, M, cur;
    cin >> K;
    while (K--) {
        cin >> P >> M;
        bool chair[501] = {false, };
        int answer = 0;

        while (P--) {
            cin >> cur;
            if (chair[cur]) answer++;
            else chair[cur] = true;
        }
        cout << answer << '\n';
    }    
    return 0;
}