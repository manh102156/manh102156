n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

check = 1
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            check = 0

if(check == 1):
    print("YES")
else:
    print("NO")