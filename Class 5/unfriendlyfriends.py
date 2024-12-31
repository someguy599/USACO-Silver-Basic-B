def minimum_photos(n, pairs):
    pairs = [(min(a, b), max(a, b)) for a, b in pairs]
    cnt = 0  
    left = 1  

    while left <= n:
        right = n  
        for a, b in pairs:
            if left <= a and right >= b:  
                right = b - 1  

        cnt += 1
        left = right + 1

    return cnt

N, K = map(int, input().split())  
pairs = []

for i in range(K):
    a, b = map(int, input().split())  
    pairs.append((a, b))  

print(minimum_photos(N, pairs))