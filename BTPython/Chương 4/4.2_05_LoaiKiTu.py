# Viết chương trình nhập một xâu kí tự từ bàn phím.
# Kiểm tra xem trong xâu có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường, bao nhiêu chữ số.
# Hiển thị các kết quả ra màn hình

import re
s = input().strip()
cap = re.findall("[A-Z]", s)
nor = re.findall("[a-z]", s)
num = re.findall("\d", s)
print("Ki tu hoa: {} chu cai\nKi tu thuong: {} chu cai\nSo: {} chu so".format(len(cap), len(nor), len(num)))