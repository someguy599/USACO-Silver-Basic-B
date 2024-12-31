M, N = map(int, input().split())  
grid = [[""] * M for i in range(N)]  


def floodfill(x, y):
    global grid
    global tempRes
    xD = [-1, 0, 1, 0] 
    yD = [0, 1, 0, -1] 
    
    grid[x][y] = '.'  
    tempRes += 1
    
    for i in range(4):
        xx = x + xD[i]
        yy = y + yD[i]
        
        if xx < 0 or xx >= N or yy < 0 or yy >= M:
            continue
        if grid[xx][yy] != "*":
            continue
        floodfill(xx, yy)

for i in range(N):
    grid[i] = list(input())

res = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == "*":
            tempRes = 0
            floodfill(i, j)
            res = max(res, tempRes)

print(res)
