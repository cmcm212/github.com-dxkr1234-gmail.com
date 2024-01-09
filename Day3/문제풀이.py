# 국어, 영어 점수를 입력받아 합계와 평균을 출력 

# 합계 : 70점, 평균 : 75점
# 합하기 위해서는 숫자여야한다.
"""
kor = int(input("국어 점수 : ")) 
eng = int(input("영어 점수 : "))
hap = kor + eng
avg = hap/2
print("합계 : " + str(hap) +"점, 평균 : " + str(avg) +"점")
# 변수도 타입이 있어서 숫자 + 문자열 성립 안된다.
# f-문자열
print(f'합계 : {hap}점, 평균 : {avg}점')
"""

# 집의 가로와 세로를 입력받아 너비를 평으로 출력하시오.
# 3.3제곱미터가 1평
"""
house_width = int(input("가로 길이 : "))
house_length = int(input("세로 길이 : "))
house_space = house_width*house_length
constant = 3.3
house_area = house_space/constant

print(house_area)
"""
# 헷갈리면 무조건 변수로 만들어라. 그리고 계속 나오는 코드는 외워라.

# 월급을 입력받아 연봉을 출력하시오 
"""salary = int(input("월급 입력 : "))
month = 12
mo = salary*month
print(mo)
"""
# 월급을 입력받아 1년치 소득세(118.8)와 소득세를 제외한 실수령액 출력 
# 연봉 실수령액(3481.2) 출력
# 소득세율은 3.3%

"""
salary = int(input("월급 입력 : "))
month = 12
money = salary*month
INCOME_RATE =3.3 * 0.01
income_tax  = money * INCOME_RATE
print(income_tax)
real_salary =  money - income_tax 
print(real_salary)
"""

# 파이썬에는 퍼센트 타입 없음 
# 연봉은 12 * 월급
# 소득세 : 연봉 * (3.3 * 0.01 = 0.033)
# 실수령액 : 연봉 - 소득세 

# 입력 처리 출력 순으로 이루어져있다.

"""
month_salary = int(input("월급 : "))
MONTH = 12
salary = month_salary * MONTH
INCOME_RATE = 3.3 * 0.01
income_tax = salary * INCOME_RATE
real_money = salary- income_tax
print(real_money)
"""

# 반지름을 입력받아 원의 면적(파이 * 반지름^2)을 출력
# 반지름을 입력받아 원둘레(2*파이*반지름)을 출력

radius = int(input("반지름 : "))
PIE = 3.14
e = 2
area = radius* radius * PIE
round = e * PIE * radius
print(f'반지름은 {radius}이며, 원의 면적은 {area}, 원의 둘레는 {round}다.')
