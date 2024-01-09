"""name = input("이름 : ")
age = input("나이 : ")
print(f"이름 : {name}이고, 나이 : {age}")
print("이름 : " + name + " 나이 : " + age)
"""
# 함수는 1가지 일만 담당한다.
# input -> 입력만 받는다.

# input으로 값을 받아오면 타입은 항상 문자열로 취급받는다. 그래서 타입을 바꿔줘야한다.
# 키보드로 입력한 것은 다 str이다. 무조건 str로 인식한다. 그렇기때문에 str이 아니면 알아서 타입을 바꿔야한다. 

# val1= None -> 지금은 값이 없다. 나중에 받아옴.
# 정의 = 변수를 생성
val1 = None 

num1 = input("숫자1 : ")
num2 = input("숫자2 : ")
# val2 = int(input('두번째 숫자 : ')) 이렇게 사용해도 된다. 근데 이게 더 좋다. 왜냐하면 나중에 또 사용할지 모르기 때문이다.

print(type(num1))
print(int(num1)+ int(num2))

sum = int(num1) + int(num2)
print(sum)

# 코드를 작성할 때, 무조건 다 작성하는게 아니라 조금씩 작성하고 실행해보고 한다.
