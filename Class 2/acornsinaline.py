def merge_sort(A, L, R):
    global traveled
    if R - L <= 1:
        if A[R] < A[L]:
            A[L], A[R] = A[R], A[L]
            traveled += abs(L - R)
        return
    
    mid = (L + R) // 2
    merge_sort(A, L, mid)
    merge_sort(A, mid + 1, R)
    
    left = A[L:mid + 1]
    right = A[mid + 1:R + 1]
    
    if right[0] < left[0]:
        for i in range(mid - L + 1):
            A[L + i], A[mid + 1 + i] = A[mid + 1 + i], A[L + i]
            traveled += abs((L + i) - (mid + 1 + i))
    return


N = int(input())
A = []
for num in range(2 ** N):
    A.append(int(input().strip()))

traveled = 0

merge_sort(A, 0, (2 ** N) - 1)

print(traveled*2)
for a in A:
    print(a)
