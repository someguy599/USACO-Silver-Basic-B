N = int(input())
line = []

for i in range(N):
    value = int(input())
    line.append(value)

balance = 0
debt = 0
distance = 1
current_pos = 0
debted = []

while current_pos < N:
    current_value = line[current_pos]
    #print("currently ", current_pos, current_value)
    if current_value > 0:
        balance += current_value
        line[current_pos] = 0
    else:
        if balance > abs(current_value):
            balance += current_value
            if current_pos in debted:
                debt += current_value
            line[current_pos] = 0
        else:
            debt -= current_value
            debted.append(current_pos)
    
    
    if debt == 0:
        current_pos += 1 
    else:
        if debt > balance:
            current_pos += 1
        else:
            current_pos -= 1
    distance += 1 
    #print(balance, debt, distance, debted)
print(distance-1)