#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

void dfs(int node, unordered_map<int, vector<int>>& adjlist, vector<bool>& visited, vector<int>& component) {
    visited[node - 1] = true;
    component.push_back(node);

    for (int neighbor : adjlist[node]) {
        if (!visited[neighbor - 1]) {
            dfs(neighbor, adjlist, visited, component);
        }
    }
}

int main() {
    int N, M, Q;
    cin >> N >> M >> Q;

    unordered_map<int, vector<int>> adjlist;

    for (int i = 1; i <= N; ++i) {
        adjlist[i] = vector<int>();
    }

    for (int i = 0; i < M; ++i) {
        int ai, bi;
        cin >> ai >> bi;
        adjlist[ai].push_back(bi);
        adjlist[bi].push_back(ai);
    }

    vector<bool> visited(N, false);
    unordered_map<int, int> components; 
    int component_id = 0;

    for (int i = 1; i <= N; ++i) {
        if (!visited[i - 1]) {
            vector<int> component;
            dfs(i, adjlist, visited, component);
            for (int node : component) {
                components[node] = component_id;
            }
            component_id += 1;
        }
    }

    for (int i = 0; i < Q; ++i) {
        int xj, yj;
        cin >> xj >> yj;
        if (components[xj] == components[yj]) {
            cout << "Y" << endl;
        } else {
            cout << "N" << endl;
        }
    }

    return 0;
}
