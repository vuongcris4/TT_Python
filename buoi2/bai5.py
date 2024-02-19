"""Ứng dụng quản lí đăng nhập bằng mật khẩu gồm
1) Đổi mật khẩu
2) Thêm mật khẩu
3) Nhập mật khẩu
4) Thoát
"""

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
