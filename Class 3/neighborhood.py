N = int(input(""))
grid = [["."]*102 for i in range(102)]
perimeter = 0

for i in range(N):
    x, y = map(int, input().split(" "))
    grid[y][x] = '@'
    
    
for i in range(102):
    for j in range(102):
        #print(perimeter, (i, j))
        if (1 <= i <= 100) and (1<= j <=100):
            if (grid[i][j-1] == grid[i][j+1] == grid[i+1][j] == grid[i-1][j] == "@") or grid[i][j] == "@":
                continue
        if j >= 1:
            if grid[i][j-1] == "@":
                perimeter += 1
        if j <= 100:
            if grid[i][j+1] == "@":
                perimeter += 1
        if i <= 100:
            if grid[i+1][j] == "@":
                perimeter += 1
        if i >= 1:
            if grid[i-1][j] == "@":
                perimeter += 1

print(perimeter)

