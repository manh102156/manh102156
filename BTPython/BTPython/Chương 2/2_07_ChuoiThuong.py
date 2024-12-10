n = int(input())
s = 0
for i in range(1, n+1, 1):
    s += 1/(n*(n+1))
print("S = {:.5f}".format(s))