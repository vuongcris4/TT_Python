class tinh_toan:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def sum(self, *c):
        s = self.a + self.b
        for each in c:
            s += each
        return s

    def multiple(self):
        return self.a * self.b

    # def __del__(self):
    #     print("Destructor is called")


# operate = tinh_toan(2, 5)
# print(operate.sum(7, 10))
# print(operate.multiple())

# del operate

