def solution2(start, length):
    s = 0
    arr = [i for i in xrange(start, start+length**2)]
    for i in xrange(length):
        # print(arr[i*length:i*length+length-i])
        for j in arr[i*length:i*length+length-i]:
            s ^= j
    return s


# def solution(start, length):
#     def helper(x, y):
#         if x % 2 == 1:
#             x += 1
#             y -= 1
#             head = x

#     xor = 0
#     for i in xrange(length):
#         xor ^= helper(start+i*length, length-i)

def solution(start, length):
    def f(a):
        b = [a, 1, a+1, 0]
        return b[a % 4]

    def g(a, b):
        return f(b) ^ f(a-1)

    xor = 0
    for i in xrange(length):
        xor ^= g(start+(i*length),
                 start+(i*length)+length-(i+1))

    return xor


if __name__ == '__main__':
    print(solution(0, 3))
    print(solution(17, 4))
    print(solution(0, 100000))
