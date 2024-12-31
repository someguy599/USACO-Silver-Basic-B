def is_feasible(N, intervals, D):
    count = 0
    last_position = -float('inf')
    
    for a, b in intervals:
        pos = max(a, last_position + D)
        while pos <= b:
            count += 1
            last_position = pos
            if count >= N:
                return True
            pos += D
    
    return count >= N

def max_distance(N, intervals):
    intervals.sort()
    low, high = 1, 10**18 
    result = 1
    
    while low <= high:
        mid = (low + high) // 2
        if is_feasible(N, intervals, mid):
            result = mid  
            low = mid + 1  
        else:
            high = mid - 1  
    
    return result

N, M = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(M)]


print(max_distance(N, intervals))