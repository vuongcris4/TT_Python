class PEOPLE:
    def __init__(self, name, age, home):
        self.name = name
        self.age = age
        self.home = home

    def printPeopleInfo(self):
        print(f"name: {self.name}, age:{self.age}, home={self.home}")


class THPT:
    def __init__(self, toan, li, hoa):
        self.toan = toan
        self.li = li
        self.hoa = hoa

    def diemtb(self):
        return (self.toan + self.li + self.hoa) / 3


class STUDENT(PEOPLE, THPT):
    def __init__(self, sid, name, age, home, toan, li, hoa):
        self.sid = sid
        PEOPLE.__init__(self, name, age, home)
        THPT.__init__(self, toan, li, hoa)
        self.printPeopleInfo()

    def printInfo(self):
        print(f"sid={self.sid}, name={self.name}, diemtb={self.diemtb()}")
        print(f"age={self.age}, hometown={self.home}")


class LECTURER:
    def __init__(self, lid, name, age, home, luong):
        self.lid = lid
        self.name = name
        self.age = age
        self.home = home
        self.luong = luong

    def printInfo(self):
        print(f"sid={self.lid}, name={self.name}, diemtb={self.diemtb}")
        print(f"age={self.age}, luong={self.luong}")


sv = STUDENT("22139078", "Tran Duy Vuong", 20, "BinhDinh", 8, 9, 10)
# print(sv.diemtb())
sv.printInfo()
