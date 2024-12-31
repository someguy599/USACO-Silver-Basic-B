import heapq

def is_valid(k, cows, T_max):
    pq = []
    
    for i in range(k):
        heapq.heappush(pq, cows[i])
    
    max_time = 0
    i = k
    
    while pq:
        cur = heapq.heappop(pq) 
        max_time = max(max_time, cur)
    
        if i < len(cows):
            heapq.heappush(pq, cur + cows[i])
            i += 1

    return max_time <= T_max


def find_min_k(N, T_max, cows):
    lo, hi = 1, N
    res = N
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_valid(mid, cows, T_max):
            res = mid
            hi = mid - 1 
        else:
            lo = mid + 1 
    
    return res


N, T_max = map(int, input().split())
cows = []
for i in range(N):
    cows.append(int(input()))
        
result = find_min_k(N, T_max, cows)
print(result)