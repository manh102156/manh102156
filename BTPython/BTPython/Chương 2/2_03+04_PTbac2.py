a, b, c = map(int, input().split())
if a == 0:
    if (b == 0):
        if (c == 0):
            print("Phuong trinh vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:  
        kq =float(-c/b)
        print("PT co 1 nghiem: x= {:.2f}".format(kq))
else:
    delta = float(b**2 - 4*a*c)
    if delta <0:
        print("Pt vo nghiem.")
    elif delta == 0:
        kq = -b/2*a
        print("PT co nghiem kep: x1= x2= {:.2f}.".format(kq))
    else:
        x1 = (-b + delta**0.5)/2*a
        x2 = (-b - delta**0.5)/2*a
        print("PT co hai nghiem: x1= {:.2f}, x2= {:.2f}.".format(x1, x2))