def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())
s = 0
for i in range(n):
    s += fibo(i)
    print("{}".format(fibo(i)), end=" ")
print("\nS(fibo) = {}".format(s))