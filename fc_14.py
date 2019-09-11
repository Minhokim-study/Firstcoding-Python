# 기본인수값, 키워드인수
# "함수호출 자동 인수 지정
# 함수룰 호출할 때 사용자가 값을 넘겨주지 않더라도 자동으로 기본값을 사용하도록 할 때 사용
# 이 때, 기본 인수값은 *상수* 만 사용할 수 있음

def say(message, times=1) :
    print(message * times)

say('Hello') # times=1 이라는 기본인수값을 주어서, times를 넣지 않아도 실행이 됨
say('World', 5)


def func(a, b=5, c=10) :
    print("a is", a, "and b is", b, "and c is", c)

func(3,7)
func(25,c=24)
func(c=50,a=100)