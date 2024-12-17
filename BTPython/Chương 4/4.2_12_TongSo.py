import re
s = input()
x = re.findall("\d+", s)
tong = 0
for i in x:
    tong += int(i)
print(tong)