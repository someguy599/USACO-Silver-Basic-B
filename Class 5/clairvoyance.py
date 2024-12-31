N = int(input())

A = [False] * ((2*N)+1)

for i in range(N):
    x = int(input())
    A[x] = True

res = 0
sumE = 0

for i in range(1, (2*N)+1):
    if A[i]:
        sumE += 1
    else:
        if sumE > 0:
            res += 1
        sumE = max(0, sumE-1)

print(res)