MAXN = 100000
N = int(input())
A = [0] * MAXN  
temp = [0] * MAXN  

list_input = input().strip().split(" ")
index = 0
for num in list_input:
    A[index] = int(num)
    index += 1

inversion_count = 0

def merge_sort(L, R):
    global inversion_count
    if L >= R:
        return
    mid = (L + R) // 2
    merge_sort(L, mid)
    merge_sort(mid + 1, R)
    merge(L, R)

def merge(L, R):
    global inversion_count
    mid = (L + R) // 2
    i, j, k = L, mid + 1, L

    while i <= mid and j <= R:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            inversion_count += (mid - i + 1)
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
print(inversion_count)
