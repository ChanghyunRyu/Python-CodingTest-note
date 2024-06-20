def solution(phone_book):
    phone_book.sort(key=len)
    book = {phone_book[0]: True}
    for i in range(1, len(phone_book)):
        phone_number = phone_book[i]
        for j in range(len(phone_number)):
            if phone_number[:j] in book:
                return False
        book[phone_number] = True
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["1195524421", "119", "97674223"]))
print(solution(["123", "12"]))
