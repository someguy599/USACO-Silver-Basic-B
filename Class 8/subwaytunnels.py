N, M = map(int, input().split(" "))
connections = {}

def travel(station, visited):
    if station in visited:
        return
    if station not in visited:
        visited.append(station)
    
    for neighbor in connections[station]:
        travel(neighbor, visited)
        

for i in range(N):
    connections[i+1] = []

for i in range(M):
    start, end = map(int, input().split(" "))
    connections[start].append(end)
    connections[end].append(start)

visited = []
travel(1, visited)

if len(visited) == N:
    print(0)
else:
    for i in range(2, N+1):
        if i not in visited:
            print(i)
