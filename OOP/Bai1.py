# 1. Tạo class Vehicle chứa 2 thuộc tính: max _speed và mileage (số dặm/Km).
# Viêt chương trình chính tạo đối tượng mới, nhập, xuất giá trị của 2 thuộc tính này.


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(f"Max speed is {self.max_speed} km/h")
        print(f"Mileage is {self.mileage} số dặm/km")


if __name__ == "__main__":
    xe = Vehicle(50, 30)
    xe.print_vehicle()
