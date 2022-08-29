#include<iostream>

int main(int argc, char** argv)
{
    std::ios_base :: sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

	int test_case;
    int N = 0, arr[1001] = {0,};

	for(test_case = 1; test_case <= 10; ++test_case) {
        int answer = 0;

        std::cin >> N;
        for (int i = 0; i < N; i++) {
            std::cin >> arr[i];
        }
        for (int i = 2; i < N-2; i++) {
            int max_height = std::max(std::max(arr[i-2], arr[i-1]), std::max(arr[i+1], arr[i+2]));
            if (arr[i] <= max_height) continue;
            answer += arr[i] - max_height;
        }
        std::cout << "#" << test_case << " " << answer << '\n';
	}
	return 0;
}