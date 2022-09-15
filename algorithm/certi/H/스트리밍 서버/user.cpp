#define MAXLength 10000
#define MAXServer 10
#define MAXUser 10000

#include <set>
#include <algorithm>

using pii = std::pair<int, int>;

struct Node {
	int uid;
	int priority;
};

struct Compare {
	bool operator()(Node* a, Node* b) const {
		if (a->priority == b->priority) {
			return a->uid > b->uid;
		}
		return a->priority < b->priority;
	}
};

struct ServerType {
	int axis;
	int cnt;
	std::set<Node*, Compare> inclusion;
	std::set<Node*, Compare> exclusion;
};

struct UserType {
	int sidx;
	int servers[MAXServer];
	Node* node;
};

Node Pool[MAXUser * MAXServer];
int PoolCnt;
ServerType Server[MAXServer];
UserType User[MAXUser];
int Length, NumServer, Capacity;

void addInclusion(int sid, Node* node) {
	Server[sid].cnt++;
	Server[sid].inclusion.insert(node);
}

void addExclusion(int sid, Node* node) {
	Server[sid].exclusion.insert(node);
}

Node* popInclusion(int sid) {
	Server[sid].cnt--;
	Node* node = nullptr;
	if (!Server[sid].inclusion.empty()) {
		auto it = Server[sid].inclusion.begin();
		node = *it;
		Server[sid].inclusion.erase(it);
	}

	return node;
}

Node* popExclusion(int sid) {
	Node* node = nullptr;
	if (!Server[sid].exclusion.empty()) {
		auto it = prev(Server[sid].exclusion.end());
		node = *it;
		Server[sid].exclusion.erase(it);
	}

	return node;
}

void removeInclusion(int sid, Node* node) {
	Server[sid].cnt--;
	Server[sid].inclusion.erase(node);
}

void assignServer(int uid) {
	int sid = User[uid].servers[User[uid].sidx];

	addInclusion(sid, User[uid].node);
	if (Server[sid].cnt > Capacity) {
		Node* node = popInclusion(sid);

		Node* exNode = &Pool[PoolCnt++];
		*exNode = *node;
		addExclusion(sid, exNode);
		User[node->uid].sidx++;
		assignServer(node->uid);
	}
}

void updateServer(int sid) {
	Node* curr;
	for (;;) {
		curr = popExclusion(sid);
		if (curr == nullptr) return;

		int uid = curr->uid;
		if (User[uid].node == nullptr) continue;

		for (int i = 0; i < User[uid].sidx; ++i) {
			if (User[uid].servers[i] == sid) {
				int prevSid = User[uid].servers[User[uid].sidx];
				removeInclusion(prevSid, User[uid].node);
				User[uid].sidx = i;
				addInclusion(sid, User[uid].node);
				updateServer(prevSid);
				return;
			}
		}
	}
}

void init(int L, int N, int C, int axis[MAXServer]) {
	PoolCnt = 0;
	NumServer = N;
	Length = L;
	Capacity = C;

	for (int i = 0; i < NumServer; ++i) {
		Server[i].axis = axis[i];
		Server[i].cnt = 0;
		Server[i].inclusion.clear();
		Server[i].exclusion.clear();
	}
}

int add_user(int uid, int axis) {
	int maxDist = 0;
	pii serverDist[MAXServer];
	for (int i = 0; i < NumServer; ++i) {
		int len;
		if (axis < Server[i].axis)
			len = std::min(Server[i].axis - axis, Length - Server[i].axis + axis);
		else
			len = std::min(axis - Server[i].axis, Length - axis + Server[i].axis);

		serverDist[i] = std::make_pair(len, i);
		maxDist = std::max(maxDist, len);
	}

	std::sort(serverDist, serverDist + NumServer);

	for (int i = 0; i < NumServer; ++i) {
		User[uid].servers[i] = serverDist[i].second;
	}

	Node* newNode = &Pool[PoolCnt++];
	newNode->uid = uid;
	newNode->priority = maxDist;
	User[uid].sidx = 0;
	User[uid].node = newNode;
	assignServer(uid);

	return User[uid].servers[User[uid].sidx];
}

int remove_user(int uid) {
	int sid = User[uid].servers[User[uid].sidx];

	removeInclusion(sid, User[uid].node);
	User[uid].node = nullptr;

	updateServer(sid);
	return sid;
}

int get_users(int sid) {
	return Server[sid].cnt;
}