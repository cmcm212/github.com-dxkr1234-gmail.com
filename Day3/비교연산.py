# 비교연산 
kor, eng = 75, 80
print(kor> 70, kor >=70)
print(kor<70, kor<=70)
print(kor==70, kor != 70)

print('')
#논리연산
print(not kor> 70)
# 조건들을 연결 
# and : 하나만 거짓이면 거짓
# or : 하나만 참이면 참 
# 논리연산에서 조건의 순서를 잘 이용해서 사용하면 시간을 단축할 수 있다.

num = 70
# num이 0이상인지 출력
print(num>=0)

#num이 100이하
print(num<=100)

# num이 0에서 100사이인가? print(0<= num <=100) 이렇게 사용하지마라
print(  num >=0 and num<=100)

# num이 0보다 작거나 100보다 큰가?
print( num < 0 or num > 100)
# print(not(num>=0 and num<=100)) 조건을 정 반대로 만들어준다. ~보다면 미만이거나 초과다

