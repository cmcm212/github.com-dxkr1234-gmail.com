list1 = [15,20,30,90]
#list1의 길이를 재라 -> len() x 

#a = 0
#for x in list1:
#    a+=1
#    print(a)

#list1의 합계를 출력하시오  // 뭔가를 출력하라고 하면 변수를 만들어야 한다 / 잘 모르겠으면 0 넣어봐라
aaaa=0
for x in list1:
    aaaa+=x
print(aaaa)

# list1의 평균(합계/개수)을 출력하시오      // list, set, tuple (sequence)을 보면 for문

hap = 0
size = 0

for k in list1:
    hap = hap + k   # 15 35 65 155
    size = size + 1 # 1 2 3 4
print(hap/size)


# 리스트에서 70점 이상인 점수의 개수
# size = 0
# for k in list1:
#   if k>=70:
#       size=szie+1