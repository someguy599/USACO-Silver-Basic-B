N = int(input())
X = [-1] * 205
Y = [-1] * 205
P = [0] * 205
adj = [[] for i in range(205)]
visited = [False] * 205

def dfs(u):
    global cnt
    cnt += 1
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

for i in range(1, N + 1):
    x, y, power = map(int, input().split())
    X[i], Y[i], P[i] = x, y, power * power

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j:
            dist_sq = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            if dist_sq <= P[i]:
                adj[i].append(j)

res = 0
for i in range(1, N + 1):
    visited = [False] * 205
    cnt = 0
    dfs(i)
    res = max(res, cnt)

print(res)
