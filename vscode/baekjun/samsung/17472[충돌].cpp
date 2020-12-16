#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int N = 0, M = 0;
int map[10][10] = {0};
int visit[10][10] = {0};
int num_island = 2;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
vector<pair<int, int> > v;

void bfs(int x, int y, int cnt) {
    int i = 0, j = 0;
    int nx = 0, ny = 0;
    queue<pair<int,int> > q;

    q.push(make_pair(x, y));
    visit[x][y] = 1;
    map[x][y] = cnt;

    while(!q.empty()){
        for(i = 0; i < 4; i++) {
            nx = q.front().first + dx[i];
            ny = q.front().second + dy[i];

            if(nx >= 0 && nx < N && ny >= 0 && ny < M && map[nx][ny] == 1) {
                map[nx][ny] = cnt;
                q.push(make_pair(nx, ny));
                visit[nx][ny] = 1;
            }
        }
        q.pop();
    }
}

void find_island(int N, int M) {
    int i = 0;

    for(i = 0; i < v.size(); i++) {
        if(visit[v[i].first][v[i].second] == 0) bfs(v[i].first, v[i].second, num_island++);
    }
}

int main() {
    int i = 0, j = 0;

    scanf("%d %d", &N, &M);

    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            scanf("%d", &map[i][j]);
            if(map[i][j] == 1) v.push_back(make_pair(i, j));
        }
    }

    find_island(N, M);

    printf("\n");
    for(i = 0; i < N; i++) {
        for(j = 0; j < M; j++) {
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }

    return 0;
}