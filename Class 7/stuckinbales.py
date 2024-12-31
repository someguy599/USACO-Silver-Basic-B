N, startrow, startcol = map(int, input().split(" "))
startrow -= 1 
startcol -= 1 
endrow, endcol = 0, 0

rowD = [-1, 1, 0, 0]
colD = [0, 0, -1, 1]

grid = [[""]*1000 for i in range(1000)]
for i in range(N):
    row, col = map(int, input().split(" "))
    grid[row-1][col-1] = "H"

moved = [[N+1]*1000 for i in range(1000)]
moved[startrow][startcol] = 0

queue = [(startrow, startcol)]

while queue:
    currow, curcol = queue.pop(0)
    hay_moved = 0
    if grid[currow][curcol] == "H":
        hay_moved = 1
    for i in range(4):
        nxtrow = currow + rowD[i]
        nxtcol = curcol + colD[i]
        if 0 <= nxtrow < 1000 and 0 <= nxtcol < 1000:
            if moved[nxtrow][nxtcol] > moved[currow][curcol] + hay_moved:
                moved[nxtrow][nxtcol] = moved[currow][curcol] + hay_moved 
                queue.append((nxtrow, nxtcol))
                if nxtrow == endrow and nxtcol == endcol:
                    print(moved[nxtrow][nxtcol])
                    break
