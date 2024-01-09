p = [10, 20, 30]
print(type(p))
for item in p : 
    print(item)

# list -> [] tuple -> () set -> {}
    
p=['++++', 10, 20, 30]
for item in p : 
    print(item)

# 리스트는 집합이다. 즉, sequence다. 근데 sequence는 하나의 값들을 모아둔것이다. 그렇기때문에 일단은 타입 구분없이 담을 수 있다. 하지만 좋지 않다.
    

li = [10, 20, 30, 40]


print(len(li))
# len은 값 개수를 알려준다. 
# 근데 왜 len은 .을 사용하지 않는 것이지? 메소드가 아닐까? 
# 메소드는 어디에는 사용가능하지만 어디에서는 사용할 수 없다. 그래서 메소드다.
# 하지만 len은 sequence는 다 길이를 잴 수 있다. 그래서 밖으로 뺀것이다. 

# len 쓰지말고 길이를 내가 측정해보자 

print('')

i = 0
for item in li : 
    i = i + 1 
print(i)
