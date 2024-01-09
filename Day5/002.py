

lang = 'python'
# slicing
print(lang[0])
print(lang[5])
print('a' in lang)
print('a' in lang)


# 뒤에서 slicing
print(lang[-1])

string = '123456789'
# 문자열 [시작위치:끝위치+1]
print(string[1:3])

# 문자열[시작위치:끝위치+1:간격]
print(string[1::5])       #[1:] < 생략하면 끝까지

# 짝수만 출력
print(string[1::2])