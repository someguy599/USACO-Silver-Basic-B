maxN = 100005
N, M = map(int, input().split(" "))
adjlist = {}
X = []
Y = []
visited = [False] * (N + 1)

for i in range(maxN):
    adjlist[i + 1] = []

for i in range(1, N + 1):
    x, y = map(int, input().split(" "))
    X.append(x)
    Y.append(y)

for i in range(M):
    u, v = map(int, input().split(" "))
    adjlist[u].append(v)
    adjlist[v].append(u)

def dfs(u):
    minx = float('inf')
    miny = float('inf')
    maxx = 0
    maxy = 0
    
    stack = [u]
    visited[u] = True
    while stack:
        node = stack.pop(-1)
        minx = min(minx, X[node - 1])
        miny = min(miny, Y[node - 1])
        maxx = max(maxx, X[node - 1])
        maxy = max(maxy, Y[node - 1])
        for neighbor in adjlist[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    
    return 2 * (maxx - minx) + 2 * (maxy - miny)


min_perimeter = float('inf')

for i in range(1, N + 1):
    if not visited[i]:
        perimeter = dfs(i)
        min_perimeter = min(min_perimeter, perimeter)

print(min_perimeter)
