#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>

struct compare {
    bool operator() (const std::pair<int, std::pair<int, int>> &a, const std::pair<int, std::pair<int, int>> &b) const {
        if (a.first > b.first) return true;
        return false;
    }
};

int main() {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
    int N, country[101] = {0, }, point, country_id, student_id, cnt_answer = 0;
    std::set<std::pair<int, std::pair<int, int>>, compare> s;//std::greater<>> s; // point, country_id, student_id

    std::cin >> N;
    while (N--) {
        std::cin >> country_id >> student_id >> point;
        s.emplace(point, std::pair<int, int>(country_id, student_id));
    }

    auto it = s.begin();
    while (cnt_answer < 3) {
        if (country[it->second.first] < 2) {
            ++country[it->second.first];
            std::cout << it->second.first << " " << it->second.second << '\n';
            ++cnt_answer;
        }
        ++it;
    }

    return 0;
}