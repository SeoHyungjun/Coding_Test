#include <iostream>
#include <algorithm>
#include <stdlib.h>

int cow[500001], horse[500001];

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
	int test_case, T, n, m, c1, c2, i, j;
    std::string print_answer = "";
	
    std::cin>>T;
	for(test_case = 1; test_case <= T; ++test_case) {
        std::cin >> n >> m >> c1 >> c2;

        // 모든 소와 말의 위치를 봤을 때 dist(소, 말) = |c1 - c2| + |0 - 0| + |z2 - z1| = |z2 - z1|의 값이 가장 적은게 답...
        for (int i = 0; i < n; ++i) std::cin >> cow[i];
        for (int i = 0; i < m; ++i) std::cin >> horse[i];

        if (n > m) std::sort(cow, cow+n);
        else std::sort(horse, horse+m);

        int min_distance = 200000001, distance;
        int answer = 0;

        if (n <= m) {
            for (int i = 0; i < n; ++i) {
                bool flag = false;
                int right = std::lower_bound(horse, horse+m, cow[i]) - horse;
                if (right == m) --right;
                int left = std::max(0, right - 1);

                if (left == right) distance = abs(horse[left] - cow[i]);
                else {
                    int left_distance = abs(horse[left] - cow[i]);
                    int right_distance = abs(horse[right] - cow[i]);

                    if (left_distance == right_distance) flag = true;
                    distance = std::min(left_distance, right_distance);
                }
                if (distance > min_distance) continue;
                if (distance == min_distance) {
                    ++answer;
                }
                else if (distance < min_distance) {
                    answer = 1;
                    min_distance = distance;
                }
                if (flag) ++answer;
            }
        } else {
            for (int i = 0; i < m; ++i) {
                bool flag = false;
                int right = std::lower_bound(cow, cow+n, horse[i]) - cow;
                if (right == m) --right;
                int left = std::max(0, right - 1);

                if (left == right) distance = abs(cow[left] - horse[i]);
                else {
                    int left_distance = abs(cow[left] - horse[i]);
                    int right_distance = abs(cow[right] - horse[i]);

                    if (left_distance == right_distance) flag = true;
                    distance = std::min(left_distance, right_distance);
                }
                if (distance > min_distance) continue;
                if (distance == min_distance) {
                    ++answer;
                }
                else if (distance < min_distance) {
                    answer = 1;
                    min_distance = distance;
                }
                if (flag) ++answer;
            }
        }
        //std::cout << '#' << test_case << ' ' << abs(c1 - c2) + min_distance << ' ' << answer << '\n';
        print_answer += '#' + std::to_string(test_case) + ' ' + std::to_string(abs(c1 - c2) + min_distance) + ' ' + std::to_string(answer) + '\n';
	}
    std::cout << print_answer;

	return 0;
}

/*
0 3 6
-2 2 4 5

while (i <= n && j <= n) {
            int distance = abs(cow[i] - horse[j]);

            if (distance < min_distance) {
                min_distance = distance;
                answer = 1;
            } else if (distance == min_distance) {
                answer++;
            }

            if (i+1 < n && j+1 < m) {
                if (abs(cow[i+1] - horse[j]) <= abs(cow[i] - horse[j+1])) ++i;
                else ++j;
            } else if (j+1 < m) ++j;
            else ++i;
        }
*/