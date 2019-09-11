# return
# " NONE, pass, DocString
# return : 함수의 명령이 실행된 후 결과를 돌려줄 때 사용

# return 예제
'''
def maximum(x, y) :
    if x > y :
        return x
    elif x == y :
        return "두 수는 같습니다."
    else :
        return y

print(maximum(3,3))
'''
# return 문을 지정하지 않으면 return None이 실행됨
# None은 변수에 저장할 값이 없다는 것을 뜻한다
'''
def some_function() :
    pass    # 아무일도 하지 않는 함수를 만듬, return None이라고 써도 무관

print(some_function())
'''
# DocString, 설명문자열
# 프로그램에 대한 설명서를 작성
# 함수에 포함된 첫 논리적 명령행의 문자열

def print_max(x, y) :
    ''' Prints the maximum of two numbers.
                                            
    The two values must be integers '''
    x = int(x)
    y - int(y)
    if x > y :
        print(x, 'is maximum')
    else :
        print (y, 'is maximum')

print_max(3,5)
print(print_max.__doc__)    #설명문을 화면에 출력
help(print_max)             #똑같이 설명문을 화면에 출력
