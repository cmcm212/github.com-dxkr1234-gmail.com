username= input('아이디 입력 : ') # 타이핑했던 것이 변수에 들어간다. 
nai = input('나이 입력 : ')
print(type(username))
print(type(nai))
# 사용자가 입력받은 값의 타입은 문자열이다. 날짜를 입력하든, 숫자로 입력하든 무조건 문자열로 저장된다.
# 개발자가 타입을 바꿔준다. 

nai = int(nai)
print(type(nai))

a = None 
print(type(a)) # None을 a에 정의하면 타입은 NoneType이 나온다.

# 함수는 엄청 작다. 그렇기때문에 기능이 함수에 하나씩밖에 없다.

