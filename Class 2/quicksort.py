MAXN = 505
N = int(input())
A = [0] * MAXN

list_input = input().strip().split(" ")
index = 0
for num in list_input:
    A[index] = int(num)
    index += 1


def qSort(L, R):
    if L >= R:
        return

    pivot = A[R] 
    i = L - 1 

    for j in range(L, R):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]  

    A[i + 1], A[R] = A[R], A[i + 1]
    print(*A[0:N])

 
    qSort(L, i)
    qSort(i + 2, R)

qSort(0, N - 1)
