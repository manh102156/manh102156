m, n = map(int, input().split())
a = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

magic_rows = []
for i in range(m):
    row_sum = sum(a[i])
    if row_sum % 7 == 0:
        magic_rows.append(i+1)

if magic_rows:
    for row in magic_rows:
        print(row)
else:
    print("NO")