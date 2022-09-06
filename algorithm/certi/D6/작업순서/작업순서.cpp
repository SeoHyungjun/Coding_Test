#include <iostream>
#include <vector>
#include <queue>

std::queue<int> q;
std::string print_answer = "";
std::vector<int> board[1001];
int depth[1001] = {0, };

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, V, E, a, b, i;
	for(test_case = 1; test_case <= 10; ++test_case) {
        for (i = 1; i <= V; ++i) board[i].clear();

        std::cin >> V >> E;
        for (i = 0; i < E; ++i) {
            std::cin >> a >> b;
            ++depth[b];
            board[a].emplace_back(b);
        }

        for (i = 1; i <= V; ++i) if (!depth[i]) q.emplace(i);

        print_answer += "#" + std::to_string(test_case) + " ";
        while (!q.empty()) {
            int cur = q.front();
            print_answer += std::to_string(cur) + " ";
            q.pop();

            for (auto& next_v : board[cur]) {
                if (--depth[next_v]) continue;
                q.emplace(next_v);
            }
        }
        print_answer += "\n";
	}
    std::cout << print_answer;

	return 0;
}