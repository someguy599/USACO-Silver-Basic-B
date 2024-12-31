N, M = map(int, input().split())
rooms = {}
grid = [[0] * (N + 1) for i in range(N + 1)]
grid[1][1] = 2 

for i in range(1, N + 1):
    for j in range(1, N + 1):
        rooms[(i, j)] = []

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    rooms[(x1, y1)].append((x2, y2))

q = [(1, 1)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    curx, cury = q.pop(0)

    for deltax, deltay in directions:
        nx, ny = curx + deltax, cury + deltay
        if 1 <= nx <= N and 1 <= ny <= N and grid[nx][ny] == 1:
            grid[nx][ny] = 2
            q.append((nx, ny))

    for x2, y2 in rooms[(curx, cury)]:
        if grid[x2][y2] == 0:
            grid[x2][y2] = 1
            for deltax, deltay in directions:
                nx, ny = x2 + deltax, y2 + deltay
                if 1 <= nx <= N and 1 <= ny <= N and grid[nx][ny] == 2:
                    grid[x2][y2] = 2
                    q.append((x2, y2))
                    break

count = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if grid[i][j] > 0:
            count += 1

print(count)