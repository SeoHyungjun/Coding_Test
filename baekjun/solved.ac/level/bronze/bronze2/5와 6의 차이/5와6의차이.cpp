#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int change_six_to_five(std::string A, std::string B) {
    int changed_A = 0, changed_B = 0, cur;
    for (int i = 0; i < A.length(); ++i) {
        cur = A[i] - '0';
        if (cur == 6) cur = 5;  
        changed_A = changed_A * 10 + cur;
    }
    for (int i = 0; i < B.length(); ++i) {
        cur = B[i] - '0';
        if (cur == 6) cur = 5;
        changed_B = changed_B * 10 + cur;
    }

    return changed_A + changed_B;
}

int change_five_to_six(std::string A, std::string B) {
    int changed_A = 0, changed_B = 0, cur;
    for (int i = 0; i < A.length(); ++i) {
        cur = A[i] - '0';
        if (cur == 5) cur = 6;  
        changed_A = changed_A * 10 + cur;
    }
    for (int i = 0; i < B.length(); ++i) {
        cur = B[i] - '0';
        if (cur == 5) cur = 6;
        changed_B = changed_B * 10 + cur;
    }

    return changed_A + changed_B;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    std::string A, B;

    std::cin >> A >> B;
    std::cout << change_six_to_five(A, B) << " " << change_five_to_six(A, B);

    return 0;
}