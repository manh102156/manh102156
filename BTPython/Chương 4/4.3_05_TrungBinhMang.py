m, n = map(int, input().split())
a = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
t = 0
for i in range(m):
    for j in range(n):
        t += a[i][j]
tbc = round(t/(m*n), 2)
print(tbc)
for i in range(m):
    for j in range(n):
        if(a[i][j]>tbc):
            print("{} {} {}".format(a[i][j], i+1, j+1))