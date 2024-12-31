def find_char(N):
    lengths = [3]
    k = 0
    while lengths[k] < N:
        k += 1
        lengths.append(2 * lengths[k - 1] + (k + 3))
    
    def locate(N, k):
        if k == 0:
            return "moo"[N - 1]

        first_part_len = lengths[k - 1]
        middle_len = k + 3

        if N <= first_part_len: 
            return locate(N, k - 1)
        elif N <= first_part_len + middle_len:
            if N - first_part_len == 1:
                return 'm'
            else:
                return 'o'
        else: 
            return locate(N - first_part_len - middle_len, k - 1)

    return locate(N, k)


N = int(input())
print(find_char(N))
