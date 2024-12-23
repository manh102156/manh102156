import math
def can(x, n):
    kq = 0
    for i in range(n):
        kq = math.sqrt(x + kq)
    return kq+1

x, n = map(int, input().split())
s = can(x, n)
print("S = {:.5f}".format(s))