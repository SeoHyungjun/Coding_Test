#include <unordered_map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define rint register int

#define MAXM (10)
#define MAXL (11)

struct MEET {
	string name;
	int start_time, end_time, del;
	set<int> mem;
} MT[10001];
int m_idx;

set<pair<pair<int, int>, int> > users_sch[20001];
int u_idx;
unordered_map<string, int> mhash;
unordered_map<string, int> uhash;

void init() {
	m_idx = u_idx = 0;
	mhash.clear();
	uhash.clear();
}

bool exist_sch(int uid, int start, int end) {
	auto it = users_sch[uid].upper_bound({ { start,end },0 });
	auto pr = prev(it);

	if (start > pr->first.second && end < it->first.first) return false;
	return true;
}

int addMeeting(char mMeeting[MAXL], int M, char mMemberList[MAXM][MAXL], int mStartTime, int mEndTime) {
	int mid = mhash[mMeeting] = ++m_idx;
	int reg_cnt = 0;

	MT[mid].name = mMeeting;
	MT[mid].start_time = mStartTime;
	MT[mid].end_time = mEndTime;
	MT[mid].mem.clear();
	MT[mid].del = 0;

	for (rint i = 0; i < M; ++i) {
		int uid = uhash[mMemberList[i]];
		if (uid == 0) {
			uid = uhash[mMemberList[i]] = ++u_idx;
			users_sch[uid].clear();
			users_sch[uid].insert( { {-1, -1}, -1} );
			users_sch[uid].insert( { {10000, 10000}, 100000} );
			users_sch[uid].insert( { {mStartTime, mEndTime}, mid} );
			MT[mid].mem.insert(uid);
			++reg_cnt;
		}
		else if (!exist_sch(uid, mStartTime, mEndTime)) {
			users_sch[uid].insert( { {mStartTime, mEndTime}, mid} );
			MT[mid].mem.insert(uid);
			++reg_cnt;
		}
	}
	if (reg_cnt == 0) {
		MT[mid].del = 1;
		return 0;
	}
	return reg_cnt;
}

int cancelMeeting(char mMeeting[MAXL]) {
	int mid = mhash[mMeeting];
	if (mid == 0 || MT[mid].del) return 0;
	MT[mid].del = 1;

	for (auto it : MT[mid].mem) users_sch[it].erase( { {MT[mid].start_time, MT[mid].end_time}, mid} );
	return 1;
}

int changeMeetingMember(char mMeeting[MAXL], char mMember[MAXL]) {
	int mid = mhash[mMeeting];
	if (mid == 0 || MT[mid].del) return -1;
	int uid = uhash[mMember];
	if (MT[mid].mem.find(uid) == MT[mid].mem.end()) {
		if (uid == 0) {
			uid = uhash[mMember] = ++u_idx;
			users_sch[uid].clear();
			users_sch[uid].insert( { {-1, -1}, -1} );
			users_sch[uid].insert( { {10000, 10000}, 100000} );
		}
		if (exist_sch(uid, MT[mid].start_time, MT[mid].end_time)) return 2;
		MT[mid].mem.insert(uid);
		users_sch[uid].insert( { { MT[mid].start_time, MT[mid].end_time}, mid} );
		return 1;
	}
	MT[mid].mem.erase(uid);
	users_sch[uid].erase( { {MT[mid].start_time, MT[mid].end_time}, mid} );
	if (MT[mid].mem.size() == 0) MT[mid].del = 1;
	return 0;
}

int changeMeeting(char mMeeting[MAXL], int mStartTime, int mEndTime) {
	int mid = mhash[mMeeting];
	if (mid == 0 || MT[mid].del) return 0;
	for (auto uid : MT[mid].mem) users_sch[uid].erase( { { MT[mid].start_time, MT[mid].end_time}, mid} );
	MT[mid].start_time = mStartTime;
	MT[mid].end_time = mEndTime;
	int reg_cnt = 0;
	for (auto uid = MT[mid].mem.begin(); uid != MT[mid].mem.end();) {
		if (!exist_sch(*uid, mStartTime, mEndTime)) {
			users_sch[*uid].insert( { { MT[mid].start_time, MT[mid].end_time}, mid} );
			++reg_cnt;
			++uid;
		}
		else uid = MT[mid].mem.erase(uid);
	}
	if (reg_cnt == 0) MT[mid].del = 1;
	return reg_cnt;
}

void checkNextMeeting(char mMember[MAXL], int mTime, char mResult[MAXL]) {
	mResult[0] = 0;
	int uid = uhash[mMember];
	if (uid == 0) return;
	auto it = users_sch[uid].upper_bound( { { mTime, 10000}, 0} );
	if (it->first.first != 10000) {
		rint i;
		for (i = 0; i < MT[it->second].name.size(); ++i) mResult[i] = MT[it->second].name[i];
		mResult[i] = 0;
	}
}