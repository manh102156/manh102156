class NhanVien:
    def __init__(self, maSo, ten, hesoluong, phucap):
        self.maSo = maSo
        self.ten = ten
        self.hesoluong = hesoluong
        self.phucap = phucap
    def nhap(self):
        thongtin = list(map(str, input().split()))
        self.maSo = int(thongtin[0])
        self.ten = thongtin[1]
        self.hesoluong = float(thongtin[2])
        self.phucap = int(thongtin[3])
    def luong(self):
        return self.hesoluong * 2000000 + self.phucap
    def xuat(self):
        print(f"{self.maSo} {self.ten} {self.hesoluong:.2f} {self.phucap} {self.luong():.0f}")

n = int(input())
ds_nhanvien = []
for i in range(n):
    nhanvien = NhanVien(0, "", 0.0, 0)
    nhanvien.nhap()
    ds_nhanvien.append(nhanvien)

ds_nhanvien.sort(key=lambda x:x.luong())

print("Nhan vien co luong thap nhat")
ds_nhanvien[0].xuat()

print("Danh sach nhan vien da sap xep(tang dan): {}".format(n))
for nhanvien in ds_nhanvien:
    nhanvien.xuat()