
"""import random
member = []
member.append("홍길동")
member.append("전우치")
member.append("임꺽정")
member.append("심봉사")

random.shuffle(member)
print(member)
"""

# ctrl + art + shift + 위아래 -> 똑같은 글 한번에 여러개 쓰는 법
# shuffle은 섞어준다. 랜덤으로

# 1년은 몇초인지 출력

# DAY_PER_YEAR
YEAR = 365
DAY = 24
HOUR = 60
MINUTE = 60
print(YEAR* DAY * HOUR * MINUTE)


#45분간 일하고 10분씩 휴식, 전체 근무시간 480분이면 
# 휴식 시간의 합계는 얼마인가? 

times = 480//55
휴식시간합계 = times * 10 
print(휴식시간합계)

# 돌아가는 사이클 = 8 
# 쉬는 시간이 10분 
# 10분이 8번 있다. 그래서 times * 10이다. 


# 숫자를 입력받아 1의 자리까지 버리고 출력 
# 예) 3512 -> 3510 

"""
num = int(input("숫자 : "))
print((num//10)*10)
#print(num-(num%10)) 

3512 - 2 -> 3510
일의 자리를 빼면 된다. 
방법은 한개가 아니다. 

# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수 
num = int(input("숫자 : "))
SEVEN = 7
print((num//SEVEN)*SEVEN)


# 자연수를 입력받아 그 숫자보다 작은 최대의 7의 배수 
num = int(input("숫자 : "))
SEVEN = 7
#print(((num-1)//SEVEN)*SEVEN)

if num%7==0 :
    print(SEVEN*((num//7)-1))
else : 
    print((num//SEVEN)*SEVEN)

"""

# 숫자를 입력받아 양수, 음수, 0을 출력

"""
num = int(input("숫자 : "))

if num > 0 : 
    print(f"{num}은 양수")
elif num <0 :
    print(f"{num}은 음수")
else : 
    print("0") 
"""

# 점수를 입력받아 70 ~ 90점이면 "추천대상", 아니면 "대상아님"이라고 출력
"""
num = int(input("점수 : "))
if 90 >= num and 70 <=num :
    print("추천대상")
else : 
    print("대상아님")
"""

b = int(input(" 길이 : "))
C = 2.54
if b > 0 :
    b = b/C
    결과 = str(b) + '인치'
elif b < 0 :
    b = b * C
    결과 = str(b) + 'cm'

else : 
    print("양수 또는 음수를 입력해주세요")
print(결과)


# scope : 변수를 사용할 수 있는 범위 
# 블록이 스코프를 생성하는 언어 : 자바 
# 즉, if문 안에 만든 것은 if문 밖에서는 사용 불가능하다.
# 그렇기 때문에 변수 선언을 if문 밖에 해야한다.
# 자바에서는 if문이 하나의 스코프다. 또 else가 하나의 스코프다.

# 함수가 스코프를 생성하는 언어 : 파이썬
# 파이썬은 블록 상관없이 사용할 수 있다. 즉 서로 다 사용이 가능하다.

# 자바스크립트는 둘 다 가능하다. 

# let 블록이 스코프
# var 함수가 스코프
