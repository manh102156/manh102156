a, b = map(int, input().split())
if (a == 0):
    if (b == 0):
        print("VSN")
    else:
        print("VN")
else:  
    kq =float(-b/a)
    print("x= {:.2f}".format(kq))