def go(pos, current_len):
    if pos < initialLen:
        return pos
    
    if pos < current_len/2:
        return go(pos, current_len/2)
        
    elif pos == current_len/2:
        return go(pos-1, current_len/2)
    
    return go((pos-1)%(current_len/2), current_len/2)


global string
global initialLen

string, N = input().split(" ")
N = int(N)

initialLen = len(string)
finalLen = initialLen

while finalLen < N:
    finalLen *= 2

result_index = int(go(N-1, finalLen))
print(string[result_index])