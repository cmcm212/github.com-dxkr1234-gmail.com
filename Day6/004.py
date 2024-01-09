# 웹프로그래밍 : 문자열 작업이 대부분
# 빅데이터 : 숫자 작업이 대부분

# replace : 치환
str4 = "010-1111-2222"
# 함수 : 소속없는 함수 + 소속있는 method
print(len(str4))
# method : 특정 타입 소속 -> 타입은 함수도 가질 수 있다.        / java는 method만 있음
# 문자열 메소드는 새로운 문자열을 만든다.
      
str4.replace("-",".")   # . == 소속의 의미 / str4.replace < replace가 str4에 소속
# print(str4) # 1. 값이 안바뀐 이유 : 문자열은 변경 x

str4 = str4.replace("1111","xxxx")
print(str4)

# "971011-2******"
j1 = "971011-2010015"
j1 = j1.replace(j1[8:], '******')
print(j1)

str5 = "      aa       aa      "
print(str5.strip())

#bool
b1, b2, b3, b4 = True, True, True, False
# and : 하나만 거짓이면 거짓 (모두 다 참이어야 한다)
# or : 하나만 참이면 된다
print(b1 and b2 and b3)
print(b1 and b2 and b4)
print(b1 or b2 or b4)
print((b4 and b1) or (b4 or b1))


nai=30
gender='여자'
city='인천'
# 나이가 20이상이고 성별은 여자
nai>=20 and gender=='여자'
# 나이가 20이상이고 성별은 여자인 사람 또는 인천에 사는 사람
(nai>=2-0 and gender=='여자') or city=='인천'
