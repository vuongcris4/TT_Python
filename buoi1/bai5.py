# Nhập vào số kí điện (kWh). Tính tổng tiền điện.

consumption = float(input("Nhap vao so ki dien (kWh): "))
cost = 2000
if consumption < 100:
    cost = 2000
elif 100 <= consumption < 200:
    cost = 4000
else:
    cost = 9000
total_cost = consumption * cost

print("Tong tien dien la: " + str(total_cost) + " VND")
