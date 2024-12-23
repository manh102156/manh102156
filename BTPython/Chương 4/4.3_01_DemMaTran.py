m, n, k = map(int, input().split())
count = 0
for i in range(m):
    row = list(map(int, input().split()))
    count += row.count(k)
print(count)