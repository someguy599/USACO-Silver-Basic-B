N, M = map(int, input().split())
grid = [input().strip() for i in range(N)]
    
labels = [[0] * M for i in range(N)]
label_id = 1

def floodfill_label(x, y, label_id):
    coords = [(x, y)]
    labels[x][y] = label_id
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while coords:
        cx, cy = coords.pop(0)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 'X' and labels[nx][ny] == 0:
                labels[nx][ny] = label_id
                coords.append((nx, ny))

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'X' and labels[i][j] == 0:
            floodfill_label(i, j, label_id)
            label_id += 1

num_components = label_id - 1

if num_components <= 1:
    print(0)

components = {}
for i in range(1, num_components+1):
    components[i] = []

for i in range(N):
    for j in range(M):
        if labels[i][j] > 0:
            components[labels[i][j]].append((i, j))

min_distance = float('inf')
for i in range(1, num_components):
    for j in range(i + 1, num_components + 1):
        for x1, y1 in components[i]:
            for x2, y2 in components[j]:
                distance = abs(x1 - x2) + abs(y1 - y2) - 1
                min_distance = min(min_distance, distance)

print(min_distance)