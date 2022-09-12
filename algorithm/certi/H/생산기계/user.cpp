#include <unordered_map>
#include <set>

#define rint register int

std::set<std::pair<int, int>, std::greater<>> set_time;
std::unordered_map<int, int> hash_id;

void init(int N, int mId[], int mTime[]) {
    set_time.clear(); hash_id.clear();
    for (rint i = 0; i < N; ++i) {set_time.emplace(mTime[i], mId[i]); hash_id[mId[i]] = mTime[i];}
}

int add(int mId, int mTime) {
	if (hash_id.count(mId)) set_time.erase({hash_id[mId], mId});
    hash_id[mId] = mTime; set_time.emplace(mTime, mId);
    return hash_id.size();
}

int remove(int K) {
    auto it = set_time.begin();
	while (K--) {hash_id.erase(hash_id.find(it->second)); set_time.erase(it++);}
    return it->second;
}

int produce(int M) {
	rint left = 0, right = set_time.begin()->first * M, mid, can_produce;
    while (left < right) {
        mid = (left + right) / 2, can_produce = 0;
        for (auto& cur : set_time) can_produce += mid / cur.first;
        if (can_produce < M) left = mid + 1;
        else right = mid;
    }
    return left;
}