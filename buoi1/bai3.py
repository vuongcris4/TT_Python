# 3) Nhập vào cạnh hình chữ nhật, bán kính hình tròn. Tính diện tích 2 hình này.

import math

retangle_length = float(input("Chieu dai hinh chu nhat: "))
retangle_width = float(input("Chieu rong hinh chu nhat: "))
radius = float(input("Ban kinh hinh tron: "))

area_of_rectangle = (retangle_length + retangle_width) * 2
area_of_circle = math.pi * radius * radius
print("Dien tich hinh chu nhat la: " + str(area_of_rectangle))
print("Dien tich hinh tron la: " + str(area_of_circle))
