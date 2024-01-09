# input() 입력 받는 함수
# 입력 시 바로 사라지기 때문에 변수에 저장한다. 
name = input('이름 입력 : ')
print("")
print('이름 : ' + name)


# f-문자열 -> f를 사용하면 name이라는 문자열을 사용할 수 있다. f없이 사용하면 {name}이라고 출력된다.
print(f'이름은 {name}')

# {}은 글자가 아니라 변수라고 알려주는 방식이다.
my_hobby = input('취미 : ')
print(f'내 취미는 {my_hobby}')

# 문자열 + 변수 출력 가능하다. 문자열 + 숫자는 안됨.
print("국어 : " + my_hobby)
