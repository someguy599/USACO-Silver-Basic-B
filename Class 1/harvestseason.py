N = 5
endx, endy = 5, 5
K = int(input())
maze = [[0] * (N + 1) for i in range(N + 1)]
res = 0
cnt = 0
xd = [-1, 0, 1, 0]
yd = [0, 1, 0, -1]

def go(x, y):
    global res, cnt
    if x == endx and y == endy:
        if cnt == (N * N) - K:
            res += 1
        return
    for i in range(4):
        xx = x + xd[i]
        yy = y + yd[i]
        if 1 <= xx <= N and 1 <= yy <= N and maze[xx][yy] == 0:  
            maze[xx][yy] = 1  
            cnt += 1
            go(xx, yy)
            maze[xx][yy] = 0  
            cnt -= 1


for i in range(K):
    x, y = map(int, input().split())
    maze[x][y] = 1  

maze[1][1] = 1 
cnt = 1
go(1, 1)
print(res)
