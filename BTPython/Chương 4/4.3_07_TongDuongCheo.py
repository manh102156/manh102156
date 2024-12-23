n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
dcc = 0
dcp = 0
for i in range(n):
    dcc += a[i][i]
    dcp += a[i][n-i-1]

print("dcc= {}, dcp= {}".format(dcc, dcp))