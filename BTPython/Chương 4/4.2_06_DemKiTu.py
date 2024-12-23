# Viết chương trình đếm số lần xuất hiện các kí tự trong xâu cho trước
# ví dụ xâu s="nngeunuee1n", kết quả là 'n': 4, 'g':1, 'u':2, 'e' : 3, '1': 1

def DemKiTu(s):
    dem = {}
    for char in s:
        if char in dem:
            dem[char] += 1
        else:
            dem[char] = 1
    return dem

s = input().strip()
result = DemKiTu(s)
for char, count in result.items():
    print("'{}': {}".format(char, count), end=", ")