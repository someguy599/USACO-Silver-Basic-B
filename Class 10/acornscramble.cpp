#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    int A[100005];
    int indexB[100005];
    bool visited[100005] = {false};
    
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    for (int i = 1; i <= N; i++) {
        int x;
        cin >> x;
        indexB[x] = i;
    }

    int cnt = 0;
    int maxLen = 0;

    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            int curLen = 0;
            int j = i;

            while (!visited[j]) {
                visited[j] = true;
                curLen++;
                j = indexB[A[j]];
            }

            if (curLen > 1) {
                cnt++;
                maxLen = max(maxLen, curLen);
            }
        }
    }

    if (cnt == 0) {
        cout << 0 << ' ' << -1 << endl;
    } else {
        cout << cnt << ' ' << maxLen << endl;
    }

    return 0;
}
