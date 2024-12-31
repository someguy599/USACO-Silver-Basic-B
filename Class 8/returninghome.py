def bfs(connections, start, target):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        current, path = queue.pop(0)
        if current == target:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in connections[current]:
                queue.append((neighbor, path + [neighbor]))

R, F, H = map(int, input().split(" "))
connections = {}
for i in range(1, R+1):
    connections[i] = []

for i in range(F):
    start, firstend, lastend = map(int, input().split(" "))
    connections[start].append(firstend)
    connections[start].append(lastend)
    connections[start].sort()


path_to_home = bfs(connections, 1, H)

print(len(path_to_home))
for road in path_to_home:
    print(road)