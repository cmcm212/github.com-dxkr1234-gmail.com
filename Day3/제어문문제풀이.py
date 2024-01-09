kor, eng = 75, 65
# 국어, 영어 모두 70점이상이면 합격, 아니면 불합격

"""
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
if kor >= 70 and eng >= 70 :
    print("너 합격")
else :
    print("불합격")
"""
# elif나 else는 무조건 조건을 정확하게 알고있을때 사용해야한다. 


# 숫자를 입력받아 음수면 양수로, 양수면 음수로 바꿔 출력
"""
numbers = int(input("숫자 : "))
print(-numbers)

if numbers >=1 :
    numbers *=-1
    print(numbers) 
elif numbers == 0 :
    print(numbers)
else :
    numbers *=-1
    print(numbers) 
"""

# 길이를 입력받아 센티미터면 인치로, 인치면 센티미티로 변경
# 1인치 = 2.54센티미터

# 인치 = 2.54 * 센티미터 
# 센티미터 = 인치 / 2.54

"""
numbers = int(input("길이 입력 : "))
type = input("센티미터? 인치?  : ")
IN = 2.54
if type == "cm" :
    print( numbers /IN  )

elif type =="inch":
    print(numbers * IN )    

else : 
    print("cm 또는 inch를 입력하세요! ")
"""

# 임의의 가정 
# 남자의 적정체중은 키-100, 여자의 적정체중은 키-105
# 키를 입력받아 적정체중을 출력하시오.

# 성별과 키를 받아야한다. 

height = int(input("키 입력 : "))
man_woman = input("man? woman? : ")
man_height = 100
woman_height = 105
if man_woman == "man" : 
    man_h = height - man_height
    print(man_h)
elif man_woman == "woman":
    woman_h = height -woman_height
    print(woman_h)
else :
    print("남자나 여자를 입력하쇼")

