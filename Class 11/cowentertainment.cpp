#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int res;
unordered_map<int, vector<int>> adjlistsame, adjlistdif;

void dfs(int u, vector<int>& games) {
    for (int v : adjlistsame[u]) {
        if (games[v] == 0) {
            games[v] = games[u];
            dfs(v, games);
        } else if (games[v] != games[u]) {
            res = -1;
        }
    }
    for (int v : adjlistdif[u]) {
        if (games[v] == 0) {
            games[v] = 3 - games[u];
            dfs(v, games);
        } else if (games[v] == games[u]) {
            res = -1;
        }
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        char ch;
        int u, v;
        cin >> ch >> u >> v;
        if (ch == 'S') {
            adjlistsame[u].push_back(v);
            adjlistsame[v].push_back(u);
        } else {
            adjlistdif[u].push_back(v);
            adjlistdif[v].push_back(u);
        }
    }

    vector<int> games;
    
    for (int i = 0; i < N+1; i++){
        games.push_back(0);
    }
    
    int cnt = 0;
    res = 0;

    for (int i = 1; i <= N; i++) {
        if (games[i] == 0) {
            cnt += 1;
            games[i] = 1;
            dfs(i, games);
            if (res < 0) {
                break;
            }
        }
    }

    if (res < 0) {
        cout << 0 << endl;
    } else {
        cout << 1;
        for (int i = 0; i < cnt; i++){
            cout << 0;
        }
    }

    return 0;
}
