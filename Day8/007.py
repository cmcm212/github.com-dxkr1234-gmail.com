# 1에서 10까지의 합계 : 55

#result=0
#
#for x in range(1,11):
#    
#    result=result+x
#
#print(result)

# 1에서 10까지의 3의 배수 출력

#for x in range(1,11):
#    if x%3==0:
#        print(x)
#
#for x in range(1,11):
#    if x%3!=0:
#        continue;       # skip      break = 반복을 중단 / continue = 반복을 스킵    // continue 는 앞에서 사용
#    print(x)

# 1~10 사이의 3의 배수의 합계 -> 3,6,9 -> 18
#result=0

#for x in range(1,11):
#    if x%3==0:
#        result=result+x
#print(result)

# 1~100사이의 5와 7의 공배수를 출력

#for x in range(1,101):
#    if x%5==0 and x%7==0:
#        print(x)

# 1~100사이의 5의 배수와 7의 배수를 출력, 단 공배수는 제외
    
#for x in range(1,101):
#    if x%5==0 or x%7==0:
#        print(x)
#    elif x%5==0 and x%7==0:
#        

for x in range(1,101):
    if x%5==0 and x%7==0:
        continue
    
    if x%5==0 or x%7==0:
        print(x, end=" ")