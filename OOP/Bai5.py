import sys


class Book:
    def __init__(self, title="", author="", price=0):
        self.title = title
        self.author = author
        self.price = price

    def View(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book Price: {self.price} VND")
        print("_______________________")


def low_price_in_book_shelf(book_shelf: Book):
    min_price = sys.maxsize
    for book in book_shelf:
        if book.price < min_price:
            min_price = book.price
            low_price_book = book
    return low_price_book


if __name__ == "__main__":
    # Nhap du lieu 4 cuon sach
    sach1 = Book("DTCB", "co Giang", 50000)
    sach2 = Book("Mach Dien", "co Hoang", 60000)
    sach3 = Book("Mang may tinh", "thay Tung", 35000)
    sach4 = Book("Python", "thay Mr.H3", 70000)
    book_shelf = [sach1, sach2]
    book_shelf.append(sach3)
    book_shelf.append(sach4)

    # Sách có giá thấp nhất, hàm trả về object Book, dùng method View để xem
    print("\nSách có giá thấp nhất")
    low_price_in_book_shelf(book_shelf).View()  # Cách 1 tự viết
    min(book_shelf, key=lambda x: x.price).View()  # Cách 2

    # Sắp xếp sách theo giá giảm dần
    print("\nPrice sort")
    book_shelf.sort(key=lambda x: x.price, reverse=True)
    for book in book_shelf:
        book.View()
