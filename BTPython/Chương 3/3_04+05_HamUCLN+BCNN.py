def ucln(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
        
def bcnn(a, b):
    return abs(a*b) // ucln(a, b)

a, b = map(int, input().split())
print("ucln = {}, bcnn = {}".format(ucln(a, b), bcnn(a, b)))