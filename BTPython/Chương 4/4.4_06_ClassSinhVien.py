class SinhVien:
    def __init__(self, ten, ma, toan, triet, ltrc):
        self.ten = ten
        self.ma = ma
        self.toan = toan
        self.triet = triet
        self.ltrc = ltrc
    def nhap(self):
        thongtin = list(map(str, input().split()))
        self.ten = thongtin[0]
        self.ma = int(thongtin[1])
        self.toan = float(thongtin[2])
        self.triet = float(thongtin[3])
        self.ltrc = float(thongtin[4])
    def diem_tb(self):
        return (self.toan + self.triet + self.ltrc)/3
    def xuat(self):
        print(f"{self.ma} {self.ten} {self.toan:.2f} {self.triet:.2f} {self.ltrc:.2f} {self.diem_tb():.2f}")

n = int(input())
ds_sinhvien = []
for i in range(n):
    sinhvien = SinhVien("", 0, 0.0, 0.0, 0.0)
    sinhvien.nhap()
    ds_sinhvien.append(sinhvien)

print("Danh sach sinh vien hoc lai")
count = 0
for sinhvien in ds_sinhvien:
    check = 0
    if sinhvien.toan < 4:
        check += 1
    if sinhvien.triet < 4:
        check += 1
    if sinhvien.ltrc < 4:
        check += 1
    if check >=2:
        sinhvien.xuat()
        count += 1
print("Danh sach nay co {} sinh vien phai hoc lai".format(count))