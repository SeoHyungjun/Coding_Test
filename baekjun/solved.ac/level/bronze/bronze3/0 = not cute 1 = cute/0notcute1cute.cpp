#include <iostream>
using namespace std;

int main() {
    int N, cur, cnt_one = 0;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> cur;
        if (cur == 1) cnt_one++;
    }
    if (cnt_one > N - cnt_one) cout << "Junhee is cute!\n";
    else cout << "Junhee is not cute!\n";

    return 0;
}