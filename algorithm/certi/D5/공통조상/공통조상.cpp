#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

#define swap(a, b) {int t = a; a = b; b = t;}
#define MAX_NODE 10001

int depth[MAX_NODE], max_level; // = (int)floor(log2(MAX_NODE));
int ac[MAX_NODE][20];
int subtree[10001];

std::vector<int> graph[MAX_NODE];

int get_tree(int cur, int parent) {
    int num_child = 0;

    depth[cur] = depth[parent] + 1;
    ac[cur][0] = parent;
    // 나의 2^i번째 조상 == 부모의 2^(i-1)번째 조상
    for (int i = 1; i < max_level; ++i) ac[cur][i] = ac[ ac[cur][i-1] ][i-1];
    // 연결된 노드 중 부모가 아니면 자식 -> dfs로 자식 호출
    int len = graph[cur].size();
    for (int i = 0; i < len; ++i) {
        int tmp = graph[cur][i];
        if (tmp == parent) continue;
        num_child += get_tree(tmp, cur);
    }

    subtree[cur] = num_child;
    return num_child + 1;
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, V, E, a, b, i, v1, v2, lca;

	freopen("input.txt", "r", stdin);
	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> V >> E >> a >> b;
        max_level = (int)floor(log2(V));
        for (int i = 1; i <= V; ++i) graph[i].clear();

        for (i = 0; i < E; ++i) { std::cin >> v1 >> v2; graph[v1].emplace_back(v2); graph[v2].emplace_back(v1);}

        depth[0] = -1;
        get_tree(1, 0);
        if (depth[a] != depth[b]) {
            if (depth[a] > depth[b]) swap(a, b);
            for (i = max_level; i >= 0; --i) {
                if (depth[a] <= depth[ac[b][i]]) b = ac[b][i];
            }
        }

        lca = a;
        if (a != b) {
            for (i = max_level; i >= 0; --i) {
                if (ac[a][i] != ac[b][i]) {
                    a = ac[a][i];
                    b = ac[b][i];
                }
                lca = ac[a][i];
            }
        }

        std::cout << '#' << test_case << ' ' << lca << ' ' << subtree[lca] + 1 << '\n';
	}
	return 0;
}