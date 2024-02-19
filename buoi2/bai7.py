def bai2():
    # Total from 1 to n
    n = int(input("Input n: "))
    total = int((n + 1) * n / 2)
    print(f"Total from 1 to {n} is {total}")


def bai3():
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


def bai4():
    # full_name = input("Input your full name: ")
    full_name = "   NGUYEN     ly tRong   "
    full_name = " ".join([word.capitalize() for word in full_name.split()])
    print(full_name)


def bai5():
    task = 0
    while task != 4:
        f = open("password.txt", "r")
        password_database = f.read()
        print(
            """___________________________________
    Chọn chức năng cần thực hiện: 
    (1) Đổi mật khẩu
    (2) Thêm mật khẩu
    (3) Nhập mật khẩu
    (4) Thoát"""
        )
        task = int(input("Vui lòng chọn chức năng: "))
        print("\n")
        if task == 1:
            old_pass = input("Please input your old password: ") + "\n"
            if old_pass not in password_database:
                print("Wrong password!")
            else:
                new_pass = input("New password: ") + "\n"
                password_database = password_database.replace(old_pass, new_pass)
                print("Update password success!")
                f = open("password.txt", "w")
                f.write(password_database)
                f.close()

        elif task == 2:
            if len(password_database.split("\n")) > 5:
                print("Saved up to 5 passwords")
                continue
            new_pass = input("Create a password: ") + "\n"
            password_database += new_pass
            print("Create a password success!")
            f = open("password.txt", "w")
            f.write(password_database)
            f.close()

        elif task == 3:
            old_pass = input("Input password to log in: ") + "\n"
            if old_pass in password_database:
                print("Log in success!")
            else:
                print("Wrong password!")


def bai6():
    # Hiện danh sách từ điển, tra từ điển, thêm từ điển, cập nhật từ điển, xóa từ điển

    f = open("dictionary.txt", "r")
    dic = str(f.read().lower())
    # dictionary_database = [word.split(": ") for word in dic.split("\n")]

    task = 0
    while task != 6:
        print(
            """\nMenu:
    1. Hiện danh sách từ điển
    2. Tra từ điển
    3. Thêm từ điển
    4. Cập nhật từ điển
    5. Xóa từ điển
    6. Lưu và thoát"""
        )

        task = input("Chọn chức năng: ")

        if task == "1":
            print(dic)

        elif task == "2":
            search_word = input("Nhập từ cần tra: ").lower()
            if search_word not in dic:
                print("Chưa có trong từ điển")
            else:
                index = dic.find(search_word + ": ") + len(search_word + ": ")
                line_break_index = dic.find("\n", index)
                print("Nghĩa của từ là: " + dic[index : line_break_index + 1])

        elif task == "3":
            search_word = input("Nhap tu: ")
            meaning_word = input("Nhap nghia: ")
            dic = dic + search_word + ": " + meaning_word + "\n"

        elif task == "4":
            search_word = input("Nhập từ cần cập nhật: ").lower()
            if search_word not in dic:
                print("Chưa có trong từ điển")
            else:
                new_meaning_word = input("Nhập nghĩa mới: ")
                index = dic.find(search_word + ": ") + len(search_word + ": ")
                line_break_index = dic.find("\n", index)

                dic = dic[:index] + new_meaning_word + dic[line_break_index:]

        elif task == "5":
            search_word = input("Nhập từ cần xoa: ").lower()
            if search_word not in dic:
                print("Chưa có trong từ điển")
            else:
                index = dic.find(search_word + ": ")
                line_break_index = dic.find("\n", index) + 2  # 2 kí tự xuoogns dòng

                dic = dic[:index] + "" + dic[line_break_index:]

        elif task == "6":
            f = open("dictionary.txt", "w")
            f.write(dic)
            break
        else:
            print("Chọn không hợp lệ. Vui lòng chọn lại.")


print("""2. Bai 2
3. Bai 3
4. Bai 4
5. Bai 5
6. Bai 6
""")

task = int(input("Chon bai: "))
if task == 2:
    bai2()
elif task == 3:
    bai3()
elif task == 4:
    bai4()
elif task == 5:
    bai5()
elif task == 6:
    bai6()

