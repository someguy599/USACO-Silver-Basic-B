def dfs(node, adjlist, visited, component):
    visited[node - 1] = True
    component.append(node)
    
    for neighbor in adjlist[node]:
        if not visited[neighbor - 1]:
            dfs(neighbor, adjlist, visited, component)


N, M, Q = map(int, input().split(" "))
adjlist = {}

for i in range(1, N + 1):
    adjlist[i] = []

for i in range(M):
    ai, bi = map(int, input().split(" "))
    adjlist[ai].append(bi)
    adjlist[bi].append(ai)

visited = [False] * N  
components = {}  
component_id = 0 

for i in range(1, N + 1):
    if not visited[i - 1]:
        component = []
        dfs(i, adjlist, visited, component)
        for node in component:
            components[node] = component_id
        component_id += 1


for i in range(Q):
    xj, yj = map(int, input().split(" "))
    if components[xj] == components[yj]:
        print("Y")
    else:
        print("N")
