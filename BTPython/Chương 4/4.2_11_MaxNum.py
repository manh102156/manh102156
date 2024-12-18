import re
s = input()
x = re.findall("\d+", s)
maxnum = 0
for i in x:
    if (int(i)) > maxnum:
        maxnum = int(i)
print(maxnum)