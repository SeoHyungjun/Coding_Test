#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    int list[26] = {0};

    cin >> word;
    for (int i = 0; i < word.size(); i++) {
        list[word[i]-97]++;
    }
    for (int i = 0; i < 26; i++) {
        cout << list[i] << " ";
    }

    return 0;
}