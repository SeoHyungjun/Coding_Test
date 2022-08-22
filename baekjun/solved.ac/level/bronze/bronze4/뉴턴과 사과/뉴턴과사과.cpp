#include <iostream>
using namespace std;

int main() {
    int person[4] = {0}, x, y, r, answer = 0;

    cin >> person[0] >> person[1] >> person[2] >> person[3] >> x >> y >> r;
    for (int i = 0; i < 4; i++) {
        if (x == person[i]) answer = i + 1;
    }
    cout << answer;

    return 0;
}