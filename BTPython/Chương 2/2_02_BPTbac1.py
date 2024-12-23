a, b = map(int, input().split())
if a == 0:
    if b > 0:
        print("VSN")
    if b<= 0:
        print("VN")
elif a>0:
    kq = float(-b/a)
    print("x>{}".format(kq))
else:
    kq = float(-b/a)
    print("x<{}".format(kq))
