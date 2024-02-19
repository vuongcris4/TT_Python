# 2) Nhập vào điểm Tích lũy, xuất ra loại học lực tương ứng (Giỏi, khá, TB, yếu)

GPA = float(input("Input your GPA: "))

if (GPA>10 or GPA <0):
    print("Diem khong hop le")
elif (GPA >=9):
    print("Xuat sac")
elif (GPA >=8):
    print("Gioi")
elif (GPA >=6.5):
    print("Kha")
elif (GPA >=5):
    print("Trung binh")
elif (GPA >=3):
    print("Yeu")
else:
    print("kem")

