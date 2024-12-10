print("PT thu nhat:")
a1, b1, c1 = map(int, input().split())
print("PT thu hai:")
a2, b2, c2 = map(int, input().split())
d = a1*b2 - a2*b1
dx = c1*b2 - c2*b1
dy = a1*c2 - a2*c1
if d == 0:
    if dx == 0 and dy == 0:
        print("He PT vo so nghiem.")
    else:
        print("He PT vo nghiem.")
else:
    x = dx/d
    y = dy/d
    print("PT co cap nghiem (x, y) = ({:.2f}, {:.2f})".format(x, y))