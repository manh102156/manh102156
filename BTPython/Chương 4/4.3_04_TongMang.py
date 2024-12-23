m, n = map(int, input().split())
a = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
b = []
for i in range(m):
    row = list(map(int, input().split()))
    b.append(row)

t = [[a[i][j] + b[i][j] for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        print("{}".format(t[i][j]), end=" ")
    print("")