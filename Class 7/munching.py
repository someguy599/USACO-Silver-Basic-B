R, C = map(int, input().split())
grid = []
start_row, start_col = -1, -1
end_row, end_col = -1, -1

rowD = [-1, 1, 0, 0]
colD = [0, 0, -1, 1]


for i in range(R):
    row = list(input().strip())
    grid.append(row)
    for j in range(C):
        if row[j] == 'C':  
            start_row, start_col = i, j
        elif row[j] == 'B':  
            end_row, end_col = i, j

distances = [[100000] * C for i in range(R)]
distances[start_row][start_col] = 0
queue = [(start_row, start_col)]


while queue:
    cur_row, cur_col = queue.pop(0)
    for i in range(4):
        nxt_row = cur_row + rowD[i]
        nxt_col = cur_col + colD[i]

        if 0 <= nxt_row < R and 0 <= nxt_col < C and grid[nxt_row][nxt_col] != '*':
            if distances[nxt_row][nxt_col] > distances[cur_row][cur_col] + 1:
                distances[nxt_row][nxt_col] = distances[cur_row][cur_col] + 1
                queue.append((nxt_row, nxt_col))
                
                if nxt_row == end_row and nxt_col == end_col:
                    break


print(distances[end_row][end_col])
