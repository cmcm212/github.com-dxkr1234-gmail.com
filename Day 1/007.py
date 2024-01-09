# 변수 : 값을 담는 상자(이름을 가진다.)
# 다시 사용할 수 있게 하기 위해서! 
x=10

print(x)

print(type(x))
print(type(10))
# 8번코드보다 7번이 더 효율적이다.

x= x-1
print(x)

# 값을 변수에 담아서 사용한다.

# 함수, 변수 -> 이름을 가진다. -> 재사용할려고


a= 80 
jumsu = 85
# 변수는 의미있는 이름을 사용하는게 좋다.
# 코드는 쉽게 쉽게 짜야한다. 

# 성적합계는 220점이다.
SumOfallScores=220 # c언어
sumOfallScores=220 # 자바
sum_of_all_scores=220 # 파이썬

# 이름은 알아보기 쉽게, 소문자, _로 만든다.
# 키워드(예약어)는 사용할 수 없다.
# 파이썬이 사용하는 단어는 사용불가

# 당신의 일믕르 변수에 저장하시오

my_name = '정태민'
my_nai = 23
# 제 이름은 정태민
print("제 이름은", my_name)

# 나이를 1 증가시킨 다음 "나이는 23"이라고 출력

my_nai = my_nai + 1
print("나이는", my_nai, "살")

# ,은 무조건 빈칸이 생긴다. +를 이용하면 빈칸이 생기지 않는다.
# 숫자와 문자는 더 할 수 없다.

dog_name = "초코"
dog_hobby = '산책'
print("우리집 강아지 이름은 "+ dog_name +"에요")
print(dog_name +"는", dog_hobby,"을 아주 좋아해요")


salary = 3000000
print('급여 :'+ str(salary))


samsung = 78000
samsung_stock_price = samsung * 10

# a는 국어성적
print("총 평가금액 : " + str(samsung_stock_price)+"원")