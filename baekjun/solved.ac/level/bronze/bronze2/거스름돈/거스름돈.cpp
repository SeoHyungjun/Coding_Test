#include <iostream>
using namespace std;

int main() {
    int money, answer = 0;
    int check[6] = {500, 100, 50, 10, 5, 1};

    cin >> money;
    money = 1000 - money;
    for (int i = 0; i < 6; i++) {
        if (money < check[i]) continue;
        answer += money / check[i];
        money %= check[i];
    }

    cout << answer;

    return 0;
}