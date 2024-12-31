MAXN = 100005
N, M = map(int, input().split(" "))
adjlistsame = {}
adjlistdif = {}
games = [0] * (N+1)

def dfs(u):
    global res
    for v in adjlistsame[u]:
        if games[v] == 0:
            games[v] = games[u]
            dfs(v)
        elif games[v] != games[u]:
            res = -1
    for v in adjlistdif[u]:
        if games[v] == 0:
            games[v] = 3 - games[u]
            dfs(v)
        elif games[v] == games[u]:
            res = -1



for i in range(MAXN):
    adjlistsame[i] = []
    adjlistdif[i] = []

for i in range(M):
    ch, u, v = input().split(" ")
    u, v = int(u), int(v)
    if ch == 'S':
        adjlistsame[u].append(v) 
        adjlistsame[v].append(u)
    else:
        adjlistdif[u].append(v)
        adjlistdif[v].append(u)

cnt = 0 
res = 0 

for i in range(1, N+1):
    if games[i] == 0:
        cnt += 1
        games[i] = 1 
        dfs(i)
        if res < 0:
            break

if res < 0:
    print(0)
else:
    print(bin(2**cnt)[2:])