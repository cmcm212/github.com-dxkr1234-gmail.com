numbers = [1,3,5,7]

# 숫자가 numbers에 있는 지(True/False) 출력
num=7
print(num in numbers)
# 한번만 찾으면 성공, 실패는 numbers의 모든 값에 대해서 못 찾아야 함.
# 성공과 실패의 조건이 다르다 -> if ~ else~ 가 아니다.
for item in numbers:
    if item==num:
        print(True)
        isFind=True
if isFind==False:
        print(False)