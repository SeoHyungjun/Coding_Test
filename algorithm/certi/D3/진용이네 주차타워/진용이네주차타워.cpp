#include <iostream>
#include <queue>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, n, m, arr[101][2], cars[2001][2], cur;

	std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        int n, m, cnt_car = 0, answer = 0;
        std::queue<int> q;

        std::cin >> n >> m;
        for (int i = 0; i < n; ++i) {
            std::cin >> cur;
            arr[i][0] = cur;
            arr[i][1] = 0;
        }
        for (int i = 0; i < m; ++i) {
            std::cin >> cur;
            cars[i][0] = cur;
            cars[i][1] = 0;
        }

        for (int i = 0; i < m+m; ++i) {
            std::cin >> cur;
            if (cur > 0) {
                --cur;
                if (cnt_car >= n) q.push(cur);
                else {
                    ++cnt_car;
                    for (int j = 0; j < n; j++) {
                        if (arr[j][1]) continue;
                        arr[j][1] = 1;
                        cars[cur][1] = j;
                        break;
                    }
                }
            } else {
                ++cur;
                int where = cars[-cur][1];
                --cnt_car;
                cars[-cur][1] = 0;
                arr[where][1] = 0;
                answer += cars[-cur][0] * arr[where][0];

                if (q.size()) {
                    ++cnt_car;
                    for (int j = 0; j < n; j++) {
                        if (arr[j][1]) continue;
                        arr[j][1] = 1;
                        cars[q.front()][1] = j;
                        q.pop();
                        break;
                    }
                }
            }
        }
        std::cout << '#' << std::to_string(test_case) << ' ' << std::to_string(answer) << '\n';
	}

	return 0;
}