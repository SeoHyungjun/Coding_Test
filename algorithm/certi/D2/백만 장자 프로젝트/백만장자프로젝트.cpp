#include<iostream>

int arr[1000001];
long long int calculate(long long int max_val, int cnt_buy, long long int cost) {
    return max_val * cnt_buy - cost;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        int N;
        long long int answer = 0, cost = 0, max_val = -1, cnt_buy = 0;
        
        std::cin >> N;
        for (int i = 0; i < N; i++) std::cin >> arr[i];
        for (int i = N; i >= 0; i--) {
            if (arr[i] > max_val) {
                answer += calculate(max_val, cnt_buy, cost);

                max_val = arr[i];
                cnt_buy = 0;
                cost = 0;
                continue;
            }
            cnt_buy++;
            cost += arr[i];
        }
        answer += calculate(max_val, cnt_buy, cost);
        std::cout << "#" << test_case << ' ' << answer << '\n';
	}
	return 0;
}