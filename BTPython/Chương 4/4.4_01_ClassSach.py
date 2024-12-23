class Sach:
    def __init__(self, ten, so_trang, gia_tien):
        self.ten = ten
        self.so_trang = so_trang
        self.gia_tien = gia_tien
    def nhap(self):
        self.ten = input("Nhap ten sach: ")
        self.so_trang = int(input("So trang: "))
        self.gia_tien =int(input("Gia tien: "))
    def gia_tb(self):
        return self.gia_tien/self.so_trang if self.so_trang != 0 else 0
    def xuat(self):
        print(f"Sach: {self.ten}, {self.so_trang} trang, gia {self.gia_tien}d, gia trung binh/trang la {self.gia_tb():.2f}d.")
    

n = int(input())
ds_sach = []
for i in range(n):
    sach = Sach("", 0, 0.0)
    sach.nhap()
    ds_sach.append(sach)

ds_sach.sort(key=lambda x:x.gia_tb(), reverse=True)

for sach in ds_sach:
    sach.xuat()