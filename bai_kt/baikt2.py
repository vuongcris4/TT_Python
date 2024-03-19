class HUMAN:
    def __init__(self, name):
        self.name = name


class STUDENT(HUMAN):
    def __init__(self, id, name, gpa):
        super().__init__(name)
        self.id = id
        self.gpa = gpa

    def View(self):
        print(f"{self.name}, {self.id}, {self.gpa}")


class CLASSROOM:
    def __init__(self, SL):
        self.SL = SL
        self.DS = self.input_DSSV()
        print("______DSSV_______")
        self.output_DSSV()
        print("________DSSV giảm dần theo ĐTB________")
        self.descending_gpa()
        print("______Sinh viên thủ lớp______")
        self.top_classroom()

    def input_DSSV(self):
        list_students = []
        for i in range(self.SL):
            print(f"________\nStudent {i+1}")
            ten = str(input("Tên: "))
            id = str(input("MSSV: "))
            gpa = float(input("DTB: "))
            student = STUDENT(id, ten, gpa)
            list_students.append(student)
        return list_students

    def output_DSSV(self):
        for student in self.DS:
            student.View()

    def descending_gpa(self):
        self.DS.sort(key=lambda x: x.gpa, reverse=True)
        self.output_DSSV()

    def top_classroom(self):
        max(self.DS, key=lambda x: x.gpa).View()


if __name__ == "__main__":
    SL = int(input("SL: "))
    lop_hoc = CLASSROOM(SL)
