a, b = map(int, input().split())
if (a == 0):
    if (b == 0):
        print("Phuong trinh Vo so nghiem")
    else:
        print("Phuong trinh Vo nghiem")
else:  
    kq =float(-b/a)
    print("PT co 1 nghiem: x= {:.2f}".format(kq))