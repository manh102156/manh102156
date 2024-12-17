# Viết chương trình nhập vào từ bàn phím một xâu kí tự.
# Kiểm tra xem trong xâu có bao nhiêu chữ cái x, với x là một chữ cái nhập từ bàn phím.
# Hiển thị các kết quả ra màn hình

s = input().strip()
x = input().strip()
dem = 0
for i in s:
    if x == i:
        dem += 1
print("Co {} ki tu '{}' trong xau.".format(dem, x))