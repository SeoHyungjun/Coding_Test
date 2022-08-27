#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
    
    string user_input;
    cin >> user_input;

    for (int i = 0; i < user_input.size(); i++) {
        if (i == 0 || (i > 0 && user_input[i-1] == '-')) cout << user_input[i];
    }

    return 0;
}