# VarArgs 매개변수
# 튜플형(*), 딕셔너리형(**) 변수
# 임의 개수의 매개 변수 지정시 별(*) 표시로 사용

#기본인수값 사용 예
'''
def total(initial=5, *numbers, **keywords) :
    print(initial)
    print(numbers)
    print(keywords)

total(10, 1, 2, 3, vegetables=50, fruits=100,)
'''
#기본인수값 사용 예
def total(initial=5, *numbers, **keywords) :
    count = initial
    for number in numbers :     # (1, 2, 3)
        count += number         # count = (10 + 1 + 2 + 3 ) = 16
    for key in keywords :       # vegetables : 50, fruits : 100 
        count += keywords[key]  # count = (16 + 50 + 100) = 166
    return count

print(total(10, 1, 2, 3, vegetables=50, fruits=100,))