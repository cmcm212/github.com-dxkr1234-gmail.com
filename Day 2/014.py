# 숫자를 2개 입력받아 다음과 같이 출력하시오! 
# 예) 3과 8의 합은 11, 곱은 24입니다. 
"""
num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

sum = num1 + num2
product = num1 * num2

print(f"{num1}과 {num2}의 합은 {sum}, 곱은 {product}입니다.")
print(num1,"과" , num2,"의 합은", sum, "곱은", product,"입니다.")


# 숫자를 2개 입력받아 큰수와 작은수를 출력하시오.
# 예: 5와 8중 큰수는 8, 작은수는 5입니다.

num1 = int(input("첫번째 숫자 : "))
num2 =int(input("두번째 숫자 : "))
h = max(num1, num2)
l = min(num1, num2)
print(f"{num1}와 {num2}중 큰수는 {h}, 작은수는 {l}입니다.")


# 타입, 변수, 산술 연산(+, -, *,   /,//     %)
# 조건문(if문) if문 실행시키려면 tab(들여쓰기)를 해야 된다.
a= 10
if a> 5:
    print('5보다 큽니다.') 
    print('if가 참이면 동작')
else:    
    print('if와 관계없다.')   

# 파이썬에서 조건 없이 들여쓰기하면 에러난다. 무조건! 
    

money = 5000
if money>=4500:
    print("떡볶이를 먹습니다.")
    print("행복해합니다")
else :
    print("나가주세요")
print("집에 옵니다.")


# 점수를 입력받아 70점이상이면 합격, 아니면 불합격이라고 출력
# 끝나면 "수고하셨습니다."라고 출력

score = int(input("점수를 입력해주세요"))
if(score >= 70 ) :
    print("합격")
else :
    print("불합격")
print('"수고하셨습니다."')


# kor에 75, eng에 80
# 평균이 70이상이면 합격 아니면 불합격

kor, eng = 75, 80
a = (kor+eng)/2
if a >= 70:
    print("합격")
else :
    print("불합격")


kor, eng = 75, 80
kor, eng = eng, kor
성립이 된다.



# 초를 입력받아 몇분 몇초인지 출력
# 예) 210초라고 입력하면 3분 30초
"""
time = int(input("초를 입력하세요 : "))
# 분이 만약 60보다 작으면 소수 나온다. 그래서 //(몫)을 이용한다.
minutes = time // 60 
hour = time % 60

print(f"{minutes}분 {hour}초")


# 분과 초를 입력하면 초를 출력
# 코드에 값이 직접 나타나는 것 : literal (그냥 적혀있는거) 많으면 좋지 않다. 단, 꼭 필요한 상수는 어쩔 수 없다.
# 5분 10초 -> 310초 

minutes = int(input("분 : "))
seconds = int(input("초 : "))
SECONDS_PER_MINUTE = 60 
# 상수는 대문자로 (헷갈려서)
time = (minutes * SECONDS_PER_MINUTE) + seconds
print(f"{time}초")


# 몇일인지 입력받아 몇개월 며칠인지 출력
# 333일 -> 11개월 3일 
input = int(input("일수 : "))
MONTH_DAYS = 30
mon = input// MONTH_DAYS
days = input % MONTH_DAYS
print(f"{mon}개월 {days}일")
