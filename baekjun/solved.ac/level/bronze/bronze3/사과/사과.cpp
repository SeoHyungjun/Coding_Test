#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, answer = 0, student, apple;

    std::cin >> N;
    while (N--) {
        std::cin >> student >> apple;
        answer += apple - student * (apple / student);
    }

    std::cout << answer;

    return 0;
}