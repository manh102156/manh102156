a, b = map(int, input().split())
if a == 0:
    if b > 0:
        print("PT co vo so nghiem")
    if b<= 0:
        print("PT vo nghiem")
elif a>0:
    kq = float(-b/a)
    print("PT co nghiem: x>{}".format(kq))
else:
    kq = float(-b/a)
    print("PT co nghiem: x<{}".format(kq))
