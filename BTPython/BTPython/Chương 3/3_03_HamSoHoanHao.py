def sohoanhao(n):
    if n < 2:
        return False
    s = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
    return s == n

a,b = map(int, input().split())
for i in range(a, b):
    if sohoanhao(i):
        print("{}".format(i), end=" ")