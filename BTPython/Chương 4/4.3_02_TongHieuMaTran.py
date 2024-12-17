m, n = map(int, input().split())
A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)
C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
D = [[A[i][j] - B[i][j] for j in range(n)] for i in range(m)]
for row in C:
    print(row)
for row in D:
    print(row)