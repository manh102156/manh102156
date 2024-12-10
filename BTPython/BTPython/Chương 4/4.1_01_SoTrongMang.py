n, k = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))
for i in x:
    if i in a:
        print("YES")
    else:
        print("NO")
        