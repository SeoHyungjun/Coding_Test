#include <iostream>
using namespace std;

int main() {
    int cnt[101] = {0, }, cur, sum = 0;

    for (int i = 0; i < 10; i++) {
        cin >> cur;
        cnt[cur/10]++;
        sum += cur;
    }
    cout << sum / 10 << endl;

    int max_cnt = 0, max_val = 0;
    for (int i = 0; i < 101; i++) {
        if (cnt[i] > max_cnt) {
            max_cnt = cnt[i];
            max_val = i*10;
        }
    }
    cout << max_val;

    return 0;
}