"""Tạo class Bus kế thừa class Vehicle (câu 1), và có thêm 1 thuộc tính: color, có thêm
1 phương thức là showBusInfo() để hiển thị các thông tin của class. Nhập giá trị cho 1 đối tượng xe Bus
và xuất các thông tin ra để xem"""

from Bai1 import *


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, color):
        super().__init__(max_speed, mileage)
        self.color = color

    def showBusInfo(self):
        self.print_vehicle()
        print("Color is: " + self.color)

xe_bus_53 = Bus(60, 60, "xanh")
xe_bus_53.showBusInfo()
