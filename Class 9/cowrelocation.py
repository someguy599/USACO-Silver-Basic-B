n = int(input())
a = list(map(int, input().split()))
 
graph = {}
for i in range(1, n + 1):
    graph[i] = a[i - 1]

visited = [False] * (n + 1)
in_cycle = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        path = []
        current = i
        while not visited[current]:
            visited[current] = True
            path.append(current)
            current = graph[current]
        
        if current in path:
            cycle_start_index = path.index(current)
            for node in path[cycle_start_index:]:
                in_cycle[node] = True

result = sum(in_cycle)
print(result)