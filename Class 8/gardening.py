N = int(input())

degrees = [0] * N

for i in range(N-1):
    u, v = map(int, input("").split(" "))
    degrees[u-1] += 1
    degrees[v-1] += 1

print(max(degrees)+1)