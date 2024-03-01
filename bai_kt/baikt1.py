def check_product(number):
    if 100 <= number <= 200:
        print("Tốt")
    elif 50 <= number < 100:
        print("Bình thường")
    elif 1 <= number < 50:
        print("Lỗi")
    else:
        print("Sai")
        return 0
    return 1


if __name__ == "__main__":
    result = []
    index = 0
    while True:
        index += 1
        number = int(input(f"Product {index}: "))
        if number == 0:
            break
        if check_product(number) == 1:
            result.append(number)
    print(f"Total {len(result)} product valid")
    print(result)

