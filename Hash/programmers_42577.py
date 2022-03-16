# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
# LEVEL 2

def solution(phone_book):
    phone_dict = {}

    for phone_number in phone_book:
        phone_dict[phone_number] = 1

    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            if phone_number != prefix and prefix in phone_dict:  #자기 자신이 아니고 해시에 prefix가 있는경우 return false
                return False
    return True


phone_book_1 = ["119", "97674223", "1195524421"]  # false
phone_book_2 = ["123", "456", "789"]  # true
phone_book_3 = ["12", "123", "1235", "567", "88"]  # false

print(f'answer: {solution(phone_book_3)}')

# for index, value in enumerate(phone_book):
#     for index2, value2 in enumerate(phone_book):
#         if index == index2:  # 같은 값 무시
#             continue
#         length = len(value)
#
#         print(f'value: {value} len: {length}, compare: {value2}')
#         if value == value2[0:length]:  # length 까지 비교해서 같은 값인지 확
#             print("has prefix")
#             return False