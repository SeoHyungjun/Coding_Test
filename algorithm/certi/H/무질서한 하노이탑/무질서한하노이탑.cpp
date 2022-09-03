#include <iostream>
#include <algorithm>
#include <stack>

#define MAX_N 1000
struct Dinfo {
	int size;
	int cur_pos;
	bool operator < (const Dinfo &b) const {
		return size > b.size;
	}
}D[MAX_N + 1];

int d_cnt;
std::stack<int> st_bar[3];

void init(int N[3], int mDisk[3][MAX_N]) {
	for (int i = 0; i < 3; ++i) st_bar[i] = {};
	d_cnt = 0;

	for (int i = 0; i < 3; ++i) {
		for (int j = N[i] - 1; j >= 0; --j) {
			st_bar[i].push(mDisk[i][j]);
			D[d_cnt++] = { mDisk[i][j], i };
		}
	}
	std::sort(D, D + d_cnt);
}

void destroy() {}

int g_step;
int g_k;
void hanoi(int index, int to) {
	if (g_step >= g_k) return;
	while (index < d_cnt && D[index].cur_pos == to) ++index;
	if (index == d_cnt) return;
	int next = 3 - D[index].cur_pos - to;

	hanoi(index + 1, next); // index를 to로 보내기 위해 index+1이후의 블럭을 next에 쌓기
	if (g_step >= g_k) return;

	st_bar[to].push(st_bar[D[index].cur_pos].top());
	st_bar[D[index].cur_pos].pop();
	D[index].cur_pos = to;
	++g_step;

	hanoi(index + 1, to); // index를 to에 위치하고 나머지도 그 위에 쌓기
}

void go(int k, int mTop[3]) {
	g_step = 0;
	g_k = k;
	hanoi(0, 2);
	for (int i = 0; i < 3; ++i) mTop[i] = (st_bar[i].empty() ? 0 : st_bar[i].top());
}