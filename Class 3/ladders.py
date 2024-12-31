from collections import deque

N = int(input())
size = 2 * N + 5

grid = [[0] * size for i in range(size)]

x = size // 2
y = size // 2
grid[x][y] = 1

chars = input().strip()
for char in chars:
    if char == "N":
        grid[x - 1][y] = grid[x - 2][y] = 1
        x -= 2
    elif char == "S":
        grid[x + 1][y] = grid[x + 2][y] = 1
        x += 2
    elif char == "E":
        grid[x][y + 1] = grid[x][y + 2] = 1
        y += 2
    elif char == "W":
        grid[x][y - 1] = grid[x][y - 2] = 1
        y -= 2

def floodfill(x, y):
    xD = [-1, 0, 1, 0] 
    yD = [0, 1, 0, -1]
    
    q = deque([(x, y)]) 
    grid[x][y] = 2 

    while q:
        curX, curY = q.popleft()
        
        for i in range(4):
            xx, yy = curX + xD[i], curY + yD[i]
            
            
            if 0 <= xx < size and 0 <= yy < size and grid[xx][yy] == 0:
                grid[xx][yy] = 2
                q.append((xx, yy))

count = 0
for i in range(size):
    for j in range(size):
        if grid[i][j] == 0:  
            count += 1
            floodfill(i, j)

print(count - 1)