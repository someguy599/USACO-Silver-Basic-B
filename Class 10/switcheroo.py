MAXN = 100000
N, M, K = map(int, input().split())

l = [0] * 100
r = [0] * 100
p = [0] * MAXN
cc = [0] * MAXN
pos = [0] * MAXN
A = [[] for i in range(MAXN + 1)]
ans = [0] * MAXN

for i in range(M):
    lvalue, rvalue = map(int, input().split())
    l[i] = lvalue - 1
    r[i] = rvalue - 1

for i in range(N):
    p[i] = i
    for j in range(M):
        if l[j] <= p[i] <= r[j]:
            p[i] = r[j] + l[j] - p[i]

C = 1
for i in range(N):
    if cc[i] == 0:
        cc[i] = C
        A[C].append(i)
        j = p[i]
        if j != i:
            pos[j] = 1
        while j != i:
            A[C].append(j)
            cc[j] = C
            if p[j] != i:
                pos[p[j]] = 1 + pos[j]
            j = p[j]
        C += 1

for i in range(N):
    ans[A[cc[i]][(pos[i] + K) % len(A[cc[i]])]] = i

for i in range(N):
    print(ans[i] + 1)
