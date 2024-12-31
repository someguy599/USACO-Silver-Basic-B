#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;

    map<pair<int, int>, vector<pair<int, int>>> rooms;
    vector<vector<int>> grid(N + 1, vector<int>(N + 1, 0));
    
    grid[1][1] = 2;

    for (int i = 0; i < M; i++){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        rooms[{x1, y1}].push_back({x2, y2});
    }

    queue<pair<int, int>> q;
    q.push({1, 1});
    vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    while (!q.empty()){
        pair<int, int> cur = q.front();
        q.pop();
        int curx, cury;
        curx = cur.first;
        cury = cur.second;

        for (pair<int, int> direction: directions){
            int deltax, deltay, nx, ny;
            deltax = direction.first;
            deltay = direction.second;
            nx = curx + deltax;
            ny = cury + deltay;
            if (nx >= 1 && nx <= N && ny >= 1 && ny <= N && grid[nx][ny] == 1) {
                grid[nx][ny] = 2; 
                q.push({nx, ny});
            }
        }

        for(pair<int, int> pair2: rooms[{curx, cury}]){
            int x2 = pair2.first;
            int y2 = pair2.second;
            if (grid[x2][y2] == 0){
                grid[x2][y2] = 1;
                for (pair<int, int> direction: directions){
                    int deltax, deltay, nx, ny;
                    deltax = direction.first;
                    deltay = direction.second;
                    nx = x2 + deltax;
                    ny = y2 + deltay;
                    if (nx >= 1 && nx <= N && ny >= 1 && ny <= N && grid[nx][ny] == 2) {
                        grid[x2][y2] = 2; 
                        q.push({x2, y2});
                        break;
                    }
                }
            }
        }
    }

    int count = 0;
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            if (grid[i][j] > 0) {
                count += 1;
            }
        }
    }

    cout << count << endl;

    return 0;
}
