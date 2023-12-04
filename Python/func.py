# 평균을 구하는 함수를 만들어 보겠습니다

# 파이썬으로 평균 구하는 함수
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(average(numbers)) # 3.0

# 이런식으로 다른 사람들이 만들어 둔 코드를 가져와서 쓰기만 하면 됩니다.

# 헤이를 출력하는 함수 만들기 (재료가 없는 함수)
def hey(): # 함수를 선언(만들기)할 때는, 항상 뒤에 콜론(:)까지 써주세요!
	print("헤이") # 함수가 작동하는 코드는 항상 들여쓰기를 해주세요!

hey() # "헤이"를 출력하는 함수=기계 hey() 작동시키기

# a,b,c 라는 세 숫자를 더하는 함수 만들기
def sum(a,b,c): # 요리을 만들 때, 재료를 넣듯이 꼭 필요한 요소를 명시
	return a+b+c

# 함수 호출 및 변수에 저장
# 함수를 작동시키고 내보내는 결과물을 result라는 변수에 담는다
result = sum(1,2,3)
print(result)