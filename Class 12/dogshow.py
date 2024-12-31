N = int(input())
dogs = []

for i in range(N):
    x, breed_id = map(int, input().split())
    dogs.append((x, breed_id))

dogs.sort()

breed_count = {}
distinct_breeds = len(set(breed_id for x, breed_id in dogs))
left = 0
result = float('inf')
current_distinct = 0


for right in range(N):
    x, breed_id = dogs[right]

    if breed_id not in breed_count:
        breed_count[breed_id] = 0
    if breed_count[breed_id] == 0:
        current_distinct += 1
    breed_count[breed_id] += 1

    while current_distinct == distinct_breeds:
        result = min(result, dogs[right][0] - dogs[left][0])
        left_breed_id = dogs[left][1]
        breed_count[left_breed_id] -= 1
        if breed_count[left_breed_id] == 0:
            current_distinct -= 1
        left += 1

print(result)
