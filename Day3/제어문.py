# control(순서를 바꾼다.)
# 조건 : 결과가 이럴수도 저럴수도 있다. 

# jumsu가 짝수인지 홀수인지 출력해라(2의 배수)
# 10%2 -> 0
# 11%2 -> 1 

jumsu = 75 

# if 조건(식) :
#     문장1
# else : 
#     문장2

"""
if jumsu%2==0 :
    print("짝수")
else :
    print("홀수")
    print("수고하셨습니다.")


# 점수가 90점이상 우수, 70점이상 합격, 미만이면 재시험
if jumsu >= 90 :
    print("우수")
elif jumsu >= 70 :
    print("합격")
else :
    print("재시험")
"""
# 숫자를 입력받아 3의 배수인지 아닌지 출력하시오
"""
numbers = int(input("숫자 입력 : "))
if numbers % 3 == 0 :
    print("3의 배수다.")
else :
    print("아니다.")
"""

# 점수를 입력받아 90점이상이면 우수, 70점이상이면 패스, 미만이면 낙제라고 출력하시오


source = int(input("점수 입력 : "))
if source >= 90:
    print("우수")
elif source >= 70 :
    print("패스")
else :
    print("낙제")


# 반복 

"""
source = input("가위 바위 보 : ")
if source == "가위":
    print("난 보다. 내가 이겼다.")
elif source == "보자기":
    print("난 묵이다. 졌다")
elif source == "보" :
    print("난 보자기다. 넌 졌다.")
else :
    print("그런거 없어")
"""