#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    char mbti[5];

    std::cin >> mbti;

    if (mbti[0] == 'E') mbti[0] = 'I';
    else mbti[0] = 'E';

    if (mbti[1] == 'S') mbti[1] = 'N';
    else mbti[1] = 'S';

    if (mbti[2] == 'T') mbti[2] = 'F';
    else mbti[2] = 'T';

    if (mbti[3] == 'J') mbti[3] = 'P';
    else mbti[3] = 'J';

    std::cout << mbti;

    return 0;
}