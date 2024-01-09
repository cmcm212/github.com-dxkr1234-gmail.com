list1 = [1,3,5]

# 10 in list1 : 결과가 참거짓(10이 list1에 있는가?)

# list1의 원소를 하나씩 꺼내 item에 담는 반복문
for item in list1:      # item부분은 변수라서 아무거나 들어가도 됨
    print(item)

index=0
while index<3: #while 뒤에는 종료조건
    print(list1[index])
    index+=1