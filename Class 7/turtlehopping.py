M, N, M1, M2 = map(int, input().split(" "))
grid = []
for i in range(M):
    grid.append(list(map(int, input().split(" "))))

rowD = [-M1, -M1, -M2, M2, M1, M1, M2, -M2]
colD = [-M2, M2, M1, M1, M2, -M2, -M1, -M1]

startrow, startcol, endrow, endcol = -1, -1, -1, -1
rowq, colq = [], []

for i in range(M):
    for j in range(N):
        if grid[i][j] == 3:
            startrow, startcol = i, j
        elif grid[i][j] == 4:
            endrow, endcol = i, j 


distances = [[1000000] * N for i in range(M)]
distances[startrow][startcol] = 0


rowq.append(startrow)
colq.append(startcol)

while len(rowq) > 0:
    curRow = rowq.pop(0)
    curCol = colq.pop(0)
    for i in range(8):
        nxtRow = curRow + rowD[i]
        nxtCol = curCol + colD[i]
        if nxtRow < 0 or nxtRow >= M or nxtCol < 0 or nxtCol >= N:
            continue
        if grid[nxtRow][nxtCol] == 0 or grid[nxtRow][nxtCol] == 2:
            continue
        if distances[nxtRow][nxtCol] > distances[curRow][curCol] + 1:
            distances[nxtRow][nxtCol] = distances[curRow][curCol] + 1
            rowq.append(nxtRow)
            colq.append(nxtCol)
            if nxtRow == endrow and nxtCol == endcol:
                print(distances[endrow][endcol])
                break