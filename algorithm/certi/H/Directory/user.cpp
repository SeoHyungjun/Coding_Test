#define MAX_DIR 50000
#define MAX_SUB 30
#define NAME_MAXLEN 6
#define PATH_MAXLEN 1999

struct Dir {
	char name[NAME_MAXLEN + 1];
	Dir* parent;
	Dir* child[MAX_SUB];
	int cnt_child;
};
Dir dir[MAX_DIR];
Dir* root;
int total_cnt;
Dir* rm_dir;

Dir* new_dir(Dir* parent, char name[]) {
	Dir* ndir = &dir[total_cnt++];

	int i = 0;
	while (name[i] && name[i] != '/') {ndir->name[i] = name[i];++i;}
	ndir->name[i] = 0;

	ndir->parent = parent;
	if (parent) parent->child[parent->cnt_child++] = ndir;

	ndir->cnt_child = 0;

	return ndir;
}

void init(int n) {
	total_cnt = 0;
	char name[1] = {0};
	root = new_dir(nullptr, name);
}

int mystrcmp(char* a, char* b) {
	int i = 0;
	while (a[i] == b[i++]) if ((a[i] == '/' || a[i] == 0) && b[i] == 0) return i;
	return -1;
}

Dir* gotodir(char path[]) {
	Dir* current = root;
	path += 1;

	while (current) {
		if (path[0] == 0) return current;
		for (int i = 0; i < current->cnt_child; ++i) {
			Dir* ch = current->child[i];
			int len = mystrcmp(path, ch->name);
			if (len <= 0) continue;
			current = ch;
			path += len + 1;
			break;
		}
	}
	return nullptr;
}

void cmd_mkdir(char path[PATH_MAXLEN + 1], char name[NAME_MAXLEN + 1]) {
	Dir* current = gotodir(path);
	new_dir(current, name);
}

void cmd_rm(char path[PATH_MAXLEN + 1]) {
	rm_dir = gotodir(path);
	Dir* parent = rm_dir->parent;
	for (int i = 0; i < parent->cnt_child; ++i) {
		if (parent->child[i] != rm_dir) continue;
		//parent->cnt_child--;
		parent->child[i] = parent->child[--parent->cnt_child];
		break;
	}
}

void my_cp(Dir* src, Dir* dst) {
	Dir* current = new_dir(dst, src->name);
	for (int i = 0; i < src->cnt_child; ++i) my_cp(src->child[i], current);
}

void cmd_cp(char srcPath[PATH_MAXLEN + 1], char dstPath[PATH_MAXLEN + 1]) {
	Dir* src = gotodir(srcPath);
	Dir* dst = gotodir(dstPath);
	my_cp(src, dst);
}

void cmd_mv(char srcPath[PATH_MAXLEN + 1], char dstPath[PATH_MAXLEN + 1]) {
	cmd_rm(srcPath);
	Dir* dst = gotodir(dstPath);
	dst->child[dst->cnt_child++] = rm_dir;
	rm_dir->parent = dst;
}

int get_count(Dir* current) {
	int sum = current->cnt_child;
	for (int i = 0; i < current->cnt_child; ++i) sum += get_count(current->child[i]);
	return sum;
}

int cmd_find(char path[PATH_MAXLEN + 1]) {
	Dir* current = gotodir(path);
	return get_count(current);
}