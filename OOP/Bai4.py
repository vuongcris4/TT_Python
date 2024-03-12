class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        chu_vi = (self.length + self.width) * 2
        return chu_vi

    def Area(self):
        dien_tich = self.length * self.width
        return dien_tich

    def display(self):
        print(f"Chieu dai hcn: {self.length}")
        print(f"Chieu rong hcn: {self.width}")
        print(f"Chu vi hcn: {self.Perimeter()}")
        print(f"Dien tich hcn: {self.Area()}")


class RectangleVolume(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        the_tich = self.Area() * self.height
        return the_tich

    def dien_tich_toan_phan(self):
        s = self.Perimeter() * self.height + self.Area() * 2
        return s

    def display(self): 
        print()
        super().display()
        print(f"Thể tích hhcn: {self.Volume()}")
        print(f"Diện tích toàn phần hhcn: {self.dien_tich_toan_phan()}")


if __name__ == "__main__":
    hcn = Rectangle(3, 5)  
    hcn.display()

    hhcn = RectangleVolume(2, 3, 4)
    hhcn.display()
