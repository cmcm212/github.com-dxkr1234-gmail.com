# 원시타입, 내장함수 <-> import
# 개발자는 값을 검증

# str(ing) 타입

str1='10'
str2='3..14'
str3='홀짝홀짝홀짝홀짝'

#연산
print(str1 + str2)      # 문자열의 +연산은 연결
print(str1 * 10)        # 문자열의 * 연산은 반복

#인덱스 연산 -> sequence와 동일
print(str3[0])
print(str3[5])

# 슬라이싱(slicing)연산 -> seuquence와 동일
print(str3[0:3])        # 홀짝홀
print(str3[3:])         # 

str4 = "72568"
print(str4[0:3])        # 725
print(str4[1:])         # 2568      / 생락하면 끝까지
print(str4[::2])        # 758       / 간격

str5="0123456789"
# 홀수만 출력       13579
print(str5[1::2])
# 3의 배수만 출력   0369
print(str5[::3])

# 내장함수 : len / 길이재는 함수
print(len('hello'))

# 문자열은 변경 불가능 (immutable <-> mutable)

str6='hello'
list6=['h','e','l','l','o']
# str6[0]='z'   < 문자열이라서 에러
list6[0]='z'    # 변경 가능