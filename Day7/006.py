# import 005  // 이름이 숫자로 시작하면 못 가져옴

import e005     

e005.hello

from e005 import hello

hello()

# e005에 파이썬이라고 출력하는 함수를 정의하고 006.py에서 호출하시오

from e005 import py

py()

# e005.py()
# py()

def message():
    print("A")
    print("B")

# 함수는 동시에 실행되지 않는다. (한번에 하나씩 실행)
# 병렬 프로그래밍 : 함수를 동시에 실행하는 것
message()
print("C")
message()