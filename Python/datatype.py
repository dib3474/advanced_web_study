name = 'bob' # 변수에는 문자열이 들어갈 수도 있고,
num = 12 # 숫자가 들어갈 수도 있고,

is_number = True # True 또는 False -> "Boolean"형이 들어갈 수도 있습니다.

print(is_number)

# 그리고 List, Dictionary 도 들어갈 수도 있죠.
a_list = ["사과", "배", "감"]  # 리스트 안에 문자열, 숫자 섞여서 만들 수도 있어요
print(a_list[0])  # a라는 리스트의 0번째(첫번째) 값 = 사과
a_list.append('망고')
print(a_list) # ['사과', '배', '감', '망고']

a_dict = {} # 빈 딕셔너리 만들기
a_dict = {'name':'영수','age':24} # 값을 채운 딕셔너리 만들기


# a_dict의 값은? {'name':'영수','age':24}
print(a_dict)
# a_dict['name']의 값은? '영수'
print(a_dict['name'])