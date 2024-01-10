# 예외(Exception) : 실행 중 발생하는 오류
# 예외처리 : 에러가 발생했을 때 오류 메세지를 내고 정상 종료하게 함
# try : 예외가 발생할 수 있는 코드    except :

try:
    jumsu = int(input("점수 입력 : "))      # try 안에 있는 함수는 실행 될 수도 있고 안될 수도 있음

    if jumsu>=70:
        print('합격')
    else:
        print('불합격')

except:
    print('점수를 숫자로 입력하세요.')