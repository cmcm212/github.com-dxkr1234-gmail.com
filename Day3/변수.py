# 변수 = 값에다 이름 붙였다. 
# 함수 = 기능에 이름을 붙였다. 
pi = 3.14 # 값을 바꿔도 된다. 
PI = 3.14 # 대문자로 작성하면 상수라는 의미다. 값을 바꾸지 말자. 

# 나의 현재 위치 
my_current_location = '인천' # 파이썬 
myCurrentLocation = '인천' 
MyCurrentLocation = '인천'
# 언어마다 관습이 있다. 그렇기 때문에 잘 사용해야한다.

# 여러분이 삼성 주식을 5만원에 10주를 구입했다.
# 현재 내 손익금액을 출력하시오.

samsung_stock = 77700
my_samsung = 50000
stock_price = 10
sum = (samsung_stock*stock_price) - (my_samsung * stock_price)
print(f"{sum}원")

"""
stock_price = 50000
stock_count = 10
current_stock_price = 77900
평가금액 = current_stock_price * stock_count
투자금액 = stock_price * stock_count
평가손익 = 평가금액 - 투자금액
print(평가손익)
"""

# 오류 찾는 법
# 1. 코드 중에 어디가 문제인지부터 파악해라.
# 2. 중간에 print를 걸어봐라
# 3. 좁혀나가야 한다. 사방에 print()를 걸어서 몇번째까지 출력되는지 확인해봐라.