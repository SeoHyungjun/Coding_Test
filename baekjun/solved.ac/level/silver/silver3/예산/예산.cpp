#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

int arr[10000], N, M;

int sum_arr(int mid) {
    int answer = 0;

    for (int i = 0; i < N; ++i) {
        if (arr[i] >= mid) answer += mid;
        else answer += arr[i];
    }

    return answer;
}

int binary_search() {
    int start = 1, end = M, mid, cur_sum;
    
    while (start <= end) {
        mid = (start + end) / 2;

        cur_sum = sum_arr(mid);
        if (cur_sum == M) {
            return mid;
        }
        else if (cur_sum < M) {
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
    }
    return end;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];
    std::cin >> M;
    std::sort(arr, arr+N);

    if (sum_arr(M) <= M) std::cout << arr[N-1];
    else std::cout << binary_search();

    return 0;
}