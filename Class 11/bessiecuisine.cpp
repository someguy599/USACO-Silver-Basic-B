#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int main(){
    int N, K;
    cin >> N >> K;

    vector <int> A;
    unordered_map<int, unordered_set<int>> dishes, answers;
    vector <bool> visited;

    for (int i = 0; i < N; i++){
        A.push_back(i+1);
        visited.push_back(false);
        dishes[i+1].insert(i+1);
    }

    for (int i = 0; i < K; i++){
        int ai, bi;
        cin >> ai >> bi;
        ai -= 1;
        bi -= 1;
        swap(A[ai], A[bi]);

        dishes[A[ai]].insert(bi+1);
        dishes[A[bi]].insert(ai+1);
    }

    for (int i = 0; i < N; i++){
        unordered_set<int> cycle;
        if (!visited[i]){
            int j = i;
            while (!visited[j]){
                visited[j] = true;
                cycle.insert(A[j]);
                j = A[j] - 1;
            }
        }
        unordered_set<int> total;
        for (int num: cycle){
            total.insert(dishes[num].begin(), dishes[num].end());
        }
        for (int num: cycle){
            answers[num] = total;
        }
    }

    for(int i = 1; i <= N; i++){
        cout << answers[i].size() << endl;
    }


    return 0;
}