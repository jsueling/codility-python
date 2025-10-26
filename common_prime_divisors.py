# I translated the algorithm from: https://stackoverflow.com/a/34252571

def solution(A, B):

    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

    def commonPrimeDivisors(a, b):
        if a == 1 and b == 1:
            return 1
        if a == 1 or b == 1:
            return 0
        cur = gcd(a, b)
        tmp = cur
        if cur == 1:
            return 0
        while True:
            a //= cur
            if a == 1:
                break
            cur = gcd(a, cur)
            if cur == 1:
                return 0
        while True:
            b //= tmp
            if b == 1:
                return 1
            tmp = gcd(b, tmp)
            if tmp == 1:
                return 0

    return sum([commonPrimeDivisors(A[i], B[i]) for i in range(len(A))])
