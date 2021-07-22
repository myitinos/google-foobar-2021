import time


class Version(object):
    def __init__(self, s):
        self._s = s
        s = s.split('.')
        self._len = len(s)
        self.major = int(s[0])
        self.minor = int(s[1]) if self._len > 1 else 0
        self.revision = int(s[2]) if self._len > 2 else 0

    def __lt__(self, other):
        if self.major == other.major:
            if self.minor == other.minor:
                if self.revision == other.revision:
                    return self._len < other._len
                return self.revision < other.revision
            return self.minor < other.minor
        return self.major < other.major


def naive_convert(s):
    v = 0
    l = s.split('.')
    for i, _v in enumerate(l):
        v += int(_v) * (10 ** (7-(3*i)))
    v += len(l)
    return v


def solution2(l):
    return sorted(l, key=lambda x: naive_convert(x))


def solution(l):
    return [_l._s for _l in sorted([Version(s) for s in l])]


if __name__ == '__main__':

    # n = 100000
    # t0 = time.perf_counter()
    # for i in range(n):
    #     assert solution2(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == [
    #         '0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0']
    # t1 = time.perf_counter()
    # print(f'Took: {t1-t0:5.3f}')
    print(solution(["1.11", "2.0.0", "1.2",
                    "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0'])
    print(solution2(["1.11", "2.0.0", "1.2",
                     "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0'])
