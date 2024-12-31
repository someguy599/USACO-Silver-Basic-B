from collections import Counter
from bisect import bisect_left

C, N = map(int, input().split())

ms = list(int(input()) for i in range(C))

F = [tuple(map(int, input().split())) for i in range(N)]

F.sort(key=lambda x: x[1])

ms.sort()

res = 0

for a, b in F:
    idx = bisect_left(ms, a)

    if idx < len(ms) and ms[idx] <= b:
        res += 1
        ms.pop(idx)

print(res)