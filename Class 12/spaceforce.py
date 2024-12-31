A = int(input(""))
asteroids = [tuple(map(int, input("").split())) for i in range(A)]

MAX_COORD = 300

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

destruction_time = [[float('inf')] * (MAX_COORD + 1) for i in range(MAX_COORD + 1)]
for x, y, t in asteroids:
    for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= MAX_COORD and 0 <= ny <= MAX_COORD:
            destruction_time[nx][ny] = min(destruction_time[nx][ny], t)

q = [(0, 0, 0)]
visited = set()
possible = False

while q:
    q.sort()
    time, x, y = q.pop(0)

    if (x, y) in visited:
        continue

    visited.add((x, y))
        
    if time < destruction_time[x][y] and destruction_time[x][y] == float('inf'):
        print(time)
        possible = True
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= MAX_COORD and 0 <= ny <= MAX_COORD:
            if (nx, ny) not in visited and time + 1 < destruction_time[nx][ny]:
                q.append((time + 1, nx, ny))

if not possible:
    print(-1)