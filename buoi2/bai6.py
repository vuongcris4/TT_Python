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
