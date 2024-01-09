# int, float, str, bool
print(True)
print(False)
print(type(True))

# 파이썬은 True, False
# 자바스크립 true, false

# 비교 -> bool : >, >=, <, <=, ==, !=
# 조건을 따지는 것에 많이 사용된다.
# 6가지
print(5>3)
print(type(5>=3))

print(5<3)
print(type(5<=3))

print(5!=3)
print(5==3)
# 괄호가 있으면 가장 안쪽부터 계산을 하게 된다.


# 부정(not) 참을 거짓으로 거짓을 참으로
print(not True)
print(not 5>3)
print()


# 원래는 5만 있으면 int지만, not을 첨가하면 5를 참 거짓으로 바꿔버린다.
print(5)
print(not 5)
print(not 0)
print(0==True)
print()

# 파이썬에서 논리연산을 사용하면 0은 거짓, 0이 아니면 참

# not이 동작하려면 뒤에 값이 참 또는 거짓이라고 나와야한다. 

# 파이썬에서 논리연산을 사용하면 ''은 거짓이다.

print(not '')
print(not 'hello')

# 결론 : 파이썬에서 타입을 바꿀 수 있다.

