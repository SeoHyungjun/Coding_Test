#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, answer, arr[4], biggest_answer;

    std::cin >> N;
    biggest_answer = 0;
    while (N--) {
        std::cin >> arr[0] >> arr[1] >> arr[2] >> arr[3];
        std::sort(arr, arr+4);

        if (arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]) answer = 50000 + arr[0] * 5000;
        
        else if (arr[0] == arr[1] and arr[1] == arr[2]) answer = 10000 + arr[0] * 1000;
        else if (arr[1] == arr[2] and arr[2] == arr[3]) answer = 10000 + arr[1] * 1000;
        
        else if (arr[0] == arr[1] and arr[2] == arr[3]) answer = 2000 + arr[0] * 500 + arr[2] * 500;

        else if (arr[0] == arr[1]) answer = 1000 + arr[0] * 100;
        else if (arr[1] == arr[2]) answer = 1000 + arr[1] * 100;
        else if (arr[2] == arr[3]) answer = 1000 + arr[2] * 100;

        else answer = arr[3] * 100;

        biggest_answer = std::max(biggest_answer, answer);
    }
    std::cout << biggest_answer;

    return 0;
}
