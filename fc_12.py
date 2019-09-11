# 함수
# 재사용 가능한 코드의 조각

# 1. 함수를 만든다.
# 2. 만들어진 함수에 이름을 붙인다.
# 3. 원하는 곳에서 함수의 이름을 부른다.

'''
def say_hello():            #함수의 이름
    print("hello world")    #함수가 할 일

say_hello()                 #함수 호출
'''

# def + 함수이름 + ( + 매개변수들 + ) + 콜론 :
#   함수가 할 일 (명령) 1
#   함수가 할 일 (명령) 2

# 매개변수 : 함수로 넘겨지는 값들의 이름, 함수를 정의할 때 주어진 이름
# 인자 : 한수에 넘겨준 값

#매개변수를 가진 함수의 예

def print_max(a,b) :
    if a > b:
        print(a, 'is maximum')

    elif a == b:
        print(a, 'is equal to', b)
    
    else :
        print(b, 'is maximum')

print_max(44,12)

x = 5
y = 7
print_max(x,y)