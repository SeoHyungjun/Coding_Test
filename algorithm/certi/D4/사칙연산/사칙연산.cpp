#include <iostream>

struct Node {
    int val;
    bool is_oper;
    std::string oper;
    int left, right;
};

Node graph[1001];

double postorder(int cur) {
    if (!graph[cur].is_oper) return (double)graph[cur].val;

    double left_val, right_val;
    left_val = postorder(graph[cur].left);
    right_val = postorder(graph[cur].right);
    if (graph[cur].oper == "+") return left_val + right_val;
    if (graph[cur].oper == "-") return left_val - right_val;
    if (graph[cur].oper == "*") return left_val * right_val;
    return left_val / right_val;
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, N, i, nodenum, left, right;
    std::string str;

	for(test_case = 1; test_case <= 10; ++test_case) {
        std::cin >> N;
        for (i = 0; i < N; ++i) {
            std::cin >> nodenum >> str;
            if (str == "+" || str == "-" || str == "*" || str == "/") {
                std::cin >> left >> right;
                graph[nodenum].is_oper = true;
                graph[nodenum].oper = str;
                graph[nodenum].left = left;
                graph[nodenum].right = right;
            }
            else {
                graph[nodenum].val = std::stoi(str);
                graph[nodenum].is_oper = false;
            }
        }
        std::cout << "#" << test_case << " " << postorder(1) << '\n';
	}
	return 0;
}