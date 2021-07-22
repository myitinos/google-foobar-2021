
# https://stackoverflow.com/questions/61944559/efficient-algorithm-for-getting-number-of-partitions-of-integer-with-distinct-pa
def solution(n):
    G = [int(g_pow == 0) for g_pow in range(n + 1)]
    for k in range(1, n):
        G = [G[g_pow] if g_pow - k < 0 else G[g_pow] + G[g_pow - k]
             for g_pow in range(n + 1)]
    return G[n]


if __name__ == '__main__':
    print(solution(3))
    print(solution(200))
