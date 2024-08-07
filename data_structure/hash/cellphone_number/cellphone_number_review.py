def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    check_book = {}
    for phone_number in phone_book:
        flag = insert_check_book(phone_number, check_book)
        if not flag:
            return False
    return True


def insert_check_book(number, check):
    for i in range(1, len(number)):
        if number[:i] in check:
            return False
    if number not in check:
        check[number] = True
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
