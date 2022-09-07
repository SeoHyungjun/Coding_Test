#include <iostream>
#include <vector>

struct Node {
    char val;
    int left, right;
};

Node graph[101];
std::vector<std::string> buf;
std::string answer;

void inorder(int n) {
    if (graph[n].left != -1) inorder(graph[n].left);
    answer += graph[n].val;
    if (graph[n].right != -1) inorder(graph[n].right);
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, N, i, j, node_num, cnt;
    std::string cur, tmp;

	for(test_case = 1; test_case <= 10; ++test_case) {
        std::cin >> N;
        std::cin.ignore();
        for (i = 0; i < N; ++i) {
            getline(std::cin, cur);
            cnt = 1;
            tmp = "";
            buf.clear();
            for (j = 0; j < cur.length(); ++j) {
                if (cur[j] == ' ') {
                    ++cnt;
                    buf.emplace_back(tmp);
                    tmp = "";
                }
                else tmp += cur[j];
            }
            buf.emplace_back(tmp);

            node_num = stoi(buf[0]);
            graph[node_num].right = (cnt > 3) ? stoi(buf[3]) : -1;
            graph[node_num].left = (cnt > 2) ? stoi(buf[2]) : -1;
            graph[node_num].val = buf[1][0];
            while(cnt--) buf.pop_back();
        }
        answer = "";
        inorder(1);
        std::cout << "#" << test_case << " " + answer + "\n";
	}
	return 0;
}