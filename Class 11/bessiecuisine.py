N, K = map(int, input().split(" "))
A = list(range(1, N + 1))
dishes = {}

visited = [False] * N 
answers = {}

for i in range(1, N+1):
    dishes[i] = set()
    dishes[i].add(i)
    answers[i] = set()
    
for i in range(K):
    ai, bi = map(int, input().split(" "))
    ai -= 1 
    bi -= 1 
    A[ai], A[bi] = A[bi], A[ai]
    
    dishes[A[ai]].add(bi + 1)
    dishes[A[bi]].add(ai + 1) 


for i in range(N):
    if not visited[i]:
        cycle = set()
        j = i
        while not visited[j]:
            visited[j] = True
            cycle.add(A[j])
            j = A[j] - 1

        total = set()
        for num in cycle:
            total.update(dishes[num])
        for num in cycle:
            answers[num] = total

for i in range(1, N + 1):
    print(len(answers[i]))
