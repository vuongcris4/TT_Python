# Total from 1/2 to 1/2n
# Tổng của chuỗi cấp số nhân

n = int(input("Input n: "))
total = 1 - 1 / 2**n
print(total)

temp = 1
s = 0
for i in range(1, n + 1):
    temp *= 2
    s += 1 / temp
print(s)
