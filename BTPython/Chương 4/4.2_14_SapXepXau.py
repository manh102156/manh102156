import re
def sort_num_in_string(s):
    num = re.findall(r"\d+", s)
    num = sorted(map(int, num))
    result = []
    num_idx = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i].isdigit():
            result.append(str(num[num_idx]))
            while i < n and s[i].isdigit():
                i += 1
            num_idx += 1
        else:
            result.append(s[i])
            i += 1
    return "".join(result)

s = input()
print(sort_num_in_string(s))