MAXN = 5005
N, Q = map(int, input().split(" "))
adjlist = {}
for i in range(MAXN):
    adjlist[i + 1] = []

def dfs(u, p):
    global cnt
    cnt += 1
    for x in adjlist[u]:
        v = x[0]
        r = x[1]
        if v != p and r >= k:
            dfs(v, u)

for i in range(N - 1):
    u, v, r = map(int, input().split(" "))
    adjlist[u].append((v, r))
    adjlist[v].append((u, r))

for i in range(Q):
    k, v = map(int, input().split(" "))
    cnt = 0
    dfs(v, -1)
    print(cnt - 1)
