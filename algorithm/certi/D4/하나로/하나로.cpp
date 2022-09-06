#include <iostream>
#include <queue>
#include <vector>
#include <cmath>

int x[1001], y[1001];
int parent[1001];

struct info {
    long long dis;
    int i, j;

    info () {dis = -1; i = -1; j = -1;}
    info(long long d, int a, int b) {
        dis = d;
        i = a;
        j = b;
    }
};

struct compare {
    bool operator() (info& a, info& b) {
        if (a.dis == b.dis) {
            if (a.i == b.i) return a.j > b.j;
            return a.i > b.j;
        }
        return a.dis > b.dis;
    }
};

//std::priority_queue<std::pair<long long, std::pair<int, int>>, std::vector<std::pair<long long, std::pair<int, int>>>, std::less<std::pair<long long, std::pair<int ,int>>>> q;
std::priority_queue<info, std::vector<info>, compare> pq;

int get_parent(int x) {
    if (parent[x] == x) return x;
    return parent[x] = get_parent(parent[x]);
}

void union_parent(int a, int b) {
    a = get_parent(a);
    b = get_parent(b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

bool find_parent(int a, int b) {
    a = get_parent(a);
    b = get_parent(b);
    if (a == b) return true;
    return false;
}

double distance(int a, int b, double E) {
    return ((double)(x[a] - x[b])*(x[a] - x[b]) + (double)(y[a] - y[b])*(y[a] - y[b]));
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, N, i, j;
    double E;

	//freopen("input.txt", "r", stdin);
	std::cin >> T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> N;
        for (i = 0; i < N; ++i) std::cin >> x[i];
        for (i = 0; i < N; ++i) std::cin >> y[i];
        std::cin >> E;

        for (i = 0; i < N; ++i) parent[i] = i;

        for (i = 0; i < N - 1; ++i) {
            for (j = i + 1; j < N; ++j) {
                pq.emplace(info(distance(i, j, E), i, j));
            }
        }

        double answer = 0.0;
        int cnt = 0;
        //while (!pq.empty()) {
        while (cnt < N-1) {
            auto cur = pq.top();
            pq.pop();
            //std::cout << cur.dis << " " << cur.i << " " << cur.j << '\n';

            if (find_parent(cur.i, cur.j)) continue;
            answer += cur.dis;
            union_parent(cur.i, cur.j);
            ++cnt;
        }
        answer *= E;
        std::cout << "#" << test_case << " " << (long long)std::floor(answer + 0.5) << "\n";
        
        while (!pq.empty()) pq.pop();
	}
	return 0;
}

