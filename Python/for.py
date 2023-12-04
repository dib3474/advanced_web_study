fruits = ['사과','배','감','귤'] # fruits라는 과일 값이 담긴 리스트

# fruits라는 리스트의 요소를 돌아가면서 반복할건데, 
# 그 요소 중 하나를 fruit라고 할게요. fruit는 순서대로 사과/배/감/귤 이 됩니다
for fruit in fruits:
	print(fruit)

# 사과, 배, 감, 귤 하나씩 꺼내어 찍힙니다.

ages =[5, 10, 13, 23, 25, 9] # ages라는 숫자 값이 담긴 리스트

# ages라는 리스트의 요소를 돌아가면서 같은 행위를 반복할건데,
# 그 요소 중 하나를 age라고 할게요. age는 순서대로 5/10/13/23/25/9 가 됩니다
for age in ages:
	# (조건) age가 20보다 크다면
	if age > 20:
		print(f"{age}살은 성인입니다") # -> 조건이 True 면 실행
	else:
		print(f"{age}살은 청소년입니다") # -> 조건이 False 라면 실행