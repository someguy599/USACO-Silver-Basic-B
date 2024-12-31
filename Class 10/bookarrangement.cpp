#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_N = 50000;

int main() {
    int N;
    cin >> N;

    int books[MAX_N];
    int sortedBooks[MAX_N];
    int indices[MAX_N];
    bool visited[MAX_N] = {false};


    for (int i = 0; i < N; i++) {
        cin >> books[i];
        sortedBooks[i] = books[i];
    }

    sort(sortedBooks, sortedBooks + N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (books[j] == sortedBooks[i]) {
                indices[i] = j;
                break;
            }
        }
    }

    int globalMin = sortedBooks[0];

    int totalCost = 0;

    for (int i = 0; i < N; i++) {
        if (visited[i]){
            continue;
        }

        int cycleSum = 0;
        int cycleMin = 100001;
        int cycleLength = 0;
        int j = i;

        while (!visited[j]) {
            visited[j] = true;
            int bookSize = sortedBooks[j];
            cycleSum += bookSize;
            cycleMin = min(cycleMin, bookSize);
            cycleLength++;
            j = indices[j];
        }

        if (cycleLength > 1) {
            int costUsingCycleMin = cycleSum + (cycleLength - 2) * cycleMin;
            int costUsingGlobalMin = cycleSum + cycleMin + 2 * globalMin + (cycleLength - 1) * globalMin;
            totalCost += min(costUsingCycleMin, costUsingGlobalMin);
        }
    }

    cout << totalCost << endl;

    return 0;
}
