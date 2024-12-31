directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(x, y, N):
    return 0 <= x < N and 0 <= y < N

def dfs(x, y, grid, visited, N):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    perimeter = 0
    
    while stack:
        cx, cy = stack.pop()
        area += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if not in_bounds(nx, ny, N) or grid[nx][ny] == '.':
                perimeter += 1
            elif not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx, ny))
    
    return area, perimeter

N = int(input()) 
grid = [input().strip() for _ in range(N)]
    
visited = [[False] * N for _ in range(N)]
best_area = 0
best_perimeter = float('inf')
    
for i in range(N):
    for j in range(N):
        if grid[i][j] == '#' and not visited[i][j]:
            area, perimeter = dfs(i, j, grid, visited, N)
            if area > best_area or (area == best_area and perimeter < best_perimeter):
                best_area = area
                best_perimeter = perimeter
    
print(best_area, best_perimeter)