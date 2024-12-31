N, G = map(int, input().split())

visited = [False] * (N + 1)

groups = []

for i in range(G):
    group = list(map(int, input().split()))
    size = group[0]
    members = group[1:]
    groups.append(members)

invited = [1]
visited[1] = True
invited_count = 1

while invited:
    friend = invited.pop(0)
    
    for group in groups:
        if friend in group:
            invited_in_group = 0
            for member in group:
                if visited[member]:
                    invited_in_group += 1
            
            if invited_in_group >= len(group) - 1:
                for member in group:
                    if not visited[member]:
                        visited[member] = True
                        invited.append(member)
                        invited_count += 1

print(invited_count)