MAXN = 505
N = int(input())
A = [0] * MAXN
temp = [0] * MAXN

list_input = input().strip().split(" ")
index = 0
for num in list_input:
    A[index] = int(num)
    index += 1

def merge_sort(L, R):
    if L >= R:
        return
    mid = (L + R) // 2
    merge_sort(L, mid)
    merge_sort(mid + 1, R)
    merge(L, R)
    print(*A[0:N])

def merge(L, R):
    mid = (L + R) // 2
    i, j, k = L, mid + 1, L

    while i <= mid and j <= R:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1

    while j <= R: 
        temp[k] = A[j]
        j += 1
        k += 1

    for i in range(L, R + 1): 
        A[i] = temp[i]

merge_sort(0, N - 1)
