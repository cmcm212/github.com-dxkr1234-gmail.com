# 나이를 입력받아 성년여부를 리턴하는 함수

def is_adult(age:int):      # is로 시작하면 물어보는 것
    if age>=18:
        return True
    else:
        return False


age=25
if is_adult()==True:
    print("당신은 출입가능합니다.")