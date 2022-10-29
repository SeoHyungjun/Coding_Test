#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <queue>
#include <vector>

std::queue<int> q;
std::vector<int> node[50001];
bool check[50001];
int parent[50001];
int depth[50001];

int LCA(int a, int b) {
    if (depth[a] > depth[b]) std::swap(a, b);
    while (depth[a] != depth[b]) b = parent[b];

    while (a != b) {
        a = parent[a];
        b = parent[b];
    }

    return a;
}

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, U, V, cur, M;

    std::cin >> N;
    for (int i = 0; i < N - 1; ++i) {
        std::cin >> U >> V;
        node[U].emplace_back(V);
        node[V].emplace_back(U);
    }

    check[1] = true;
    q.emplace(1);

    while (!q.empty()) {
        cur = q.front();
        q.pop();

        for (int i = 0; i < node[cur].size(); ++i) {
            if (check[node[cur][i]]) continue;
            depth[node[cur][i]] = depth[cur] + 1;
            check[node[cur][i]] = true;
            parent[node[cur][i]] = cur;
            q.emplace(node[cur][i]);
        }
    }

    std::cin >> M;
    for (int i = 0; i < M; ++i) {
        std::cin >> U >> V;
        std::cout << LCA(U, V) << '\n';
    }

    return 0;
}