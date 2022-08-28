#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#define CMD_INIT 1
#define CMD_HIRE 2
#define CMD_FIRE 3
#define CMD_UPDATE_STUDENT 4
#define CMD_UPDATE_TEAM 5
#define CMD_BEST_STUDENT 6

extern void init();
extern void hire(int mID, int mTeam, int mScore);
extern void fire(int mID);
extern void updateStudent(int mID, int mScore);
extern void updateTeam(int mTeam, int mChangeScore);
extern int bestStudent(int mTeam);

/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

static bool run()
{
    int numQuery;

    int mID, mTeam, mScore, mChangeScore;

    int userAns, ans;

    bool isCorrect = false;

    scanf("%d", &numQuery);

    for (int i = 0; i < numQuery; ++i)
    {
        int cmd;
        scanf("%d", &cmd);
        switch (cmd)
        {
        case CMD_INIT:
            init();
            isCorrect = true;
            break;
        case CMD_HIRE:
            scanf("%d %d %d", &mID, &mTeam, &mScore);
            hire(mID, mTeam, mScore);
            break;
        case CMD_FIRE:
            scanf("%d", &mID);
            fire(mID);
            break;
        case CMD_UPDATE_STUDENT:
            scanf("%d %d", &mID, &mScore);
            updateStudent(mID, mScore);
            break;
        case CMD_UPDATE_TEAM:
            scanf("%d %d", &mTeam, &mChangeScore);
            updateTeam(mTeam, mChangeScore);
            break;
        case CMD_BEST_STUDENT:
            scanf("%d", &mTeam);
            userAns = bestStudent(mTeam);
            scanf("%d", &ans);
            if (userAns != ans)
            {
                isCorrect = false;
            }
            break;
        default:
            isCorrect = false;
            break;
        }
    }

    return isCorrect;
}

int main()
{
    setbuf(stdout, NULL);
    //freopen("sample_input.txt", "r", stdin);

    int T, MARK;
    scanf("%d %d", &T, &MARK);

    for (int tc = 1; tc <= T; tc++)
    {
        int score = run() ? MARK : 0;
        printf("#%d %d\n", tc, score);
    }

    return 0;
}

///////////////////////////////////////////////////////////////////////////
#include <algorithm>
using namespace std;

struct Node {
    int id, team;
    Node* prev;
    Node* next;
} student[100001];

struct List {
    Node head, tail;
} studentList[6][6];

auto link(Node* u, Node* v) {
    u->next = v;
    v->prev = u;
}

auto insert(List* list, Node* u) {
    link(list->tail.prev, u);
    link(u, &list->tail);
}

auto erase(Node* u) {
    link(u->prev, u->next);
}

auto merge(List* u, List* v) {
    if (v->head.next == &v->tail) return;
    link(u->tail.prev, v->head.next);
    link(v->tail.prev, &u->tail);
    link(&v->head, &v->tail);
}


void init(){
    for (int i = 1; i < 6; i++) {
        for (int j = 1; j < 6; j++) {
            link(&studentList[i][j].head, &studentList[i][j].tail);
        }
    }
}

void hire(int mID, int mTeam, int mScore){
    student[mID].id = mID;
    student[mID].team = mTeam;
    insert(&studentList[mTeam][mScore], &student[mID]);
}

void fire(int mID){
    erase(&student[mID]);
}

void updateStudent(int mID, int mScore){
    erase(&student[mID]);
    insert(&studentList[student[mID].team][mScore], &student[mID]);
}

void updateTeam(int mTeam, int mChangeScore){
    if (mChangeScore < 0) { 
        for (int score = 2; score < 6; score++) {
            int new_score = max(1, score + mChangeScore);
            merge(&studentList[mTeam][new_score], &studentList[mTeam][score]);
        }
    } else if (mChangeScore > 0) { 
        for (int score = 4; score > 0; score--) {
            int new_score = min(5, score + mChangeScore);
            merge(&studentList[mTeam][new_score], &studentList[mTeam][score]);
        }
    }
}

int bestStudent(int mTeam){
    for (auto group = studentList[mTeam] + 5;;group--) {
        if (group->head.next == &group->tail) continue;
        
        int answer = -1;
        for (auto student = group->head.next; student != &group->tail; student = student->next) {
            answer = max(answer, student->id);
        }
        return answer;
    }
}