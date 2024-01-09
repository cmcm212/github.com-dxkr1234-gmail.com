"""
# 섭씨를 입력받아 화씨로 출력하시오.
Celsius = int(input("섭씨 : "))
C = 1.8
T = 32
F = (Celsius * C) + T
print(f"화씨 온도 : {F}")

# 온도와 종류를 입력받으시오
# 예) 온도 : 35
# 예) 종류 : 섭씨
# 종류가 섭씨면 온도를 화씨로 변환, 아니면 섭씨로 변환 
"""

temperature = int(input("온도 : "))
kind = input("변환할 온도 종류(섭씨 또는 화씨) 입력 : ")

C = 1.8
T = 32 


if kind == "섭씨" :
    F = (temperature * C) + T
    print(f"섭씨 {temperature}는 화씨로 {F}다.")
else :
    F = (temperature-T)/C 
    print(f"화씨 {temperature}는 섭씨로 {F}다.")

# 1. 온도 입력 -> 입력 온도가 섭씨? 화씨?
# 2. 섭씨 또는 화씨를 입력받는다.
# 3. 섭씨면 화씨로 변환
    