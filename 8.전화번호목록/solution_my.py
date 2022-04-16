def solution(phone_book):
    # 접두어로 겹치는게 있으면 false, 없으면 true
    phone_book.sort(key=len)

    phone_book_set = set(phone_book)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[0:i] in phone_book_set:
                return False
    return True
