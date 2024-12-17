# Viết chương trình nhập vào 1 chuỗi các số phân cách nhau bởi dấu phẩy, in ra các số lẻ trong danh sách

s = input().strip()
numbers = s.split(",")
odd = []
for num in numbers:
    if int(num) % 2 != 0:
        if num not in odd:
            odd.append(num)
print(", ".join(odd))