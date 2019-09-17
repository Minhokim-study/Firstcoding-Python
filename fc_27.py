# 객체지향

# 절차지향 프로그래밍
    # 함수 조합
# 객체지향 프로그래밍
    # 데이터와 기능을 객체로 묶어서 구성

# 객체지향에서의 클래스와 객체
    # 클래스 (class) - 틀, 디자인 - ex) 차
    # 객체 (object) - 제품 - ex) mini, R8, Benz e300, SONATA

# 객체지향에서의 클래스의 속성
    # 클래스에 속한 변수 - 필드 (field)
    # 클래스에 속한 함수 - 메소드 (method)
    # 클래스의 인스턴스/객체에 내장된 변수
        # 인스턴스 변수 : self 에 연결 (객체와 연결된 변수)
    # 클래스 자체에 내장된 변수
        # 클래스 변수

# self
    # 클래스 메소드가 일반 함수와 다른 점
    # 클래스 안에서 만들어진 함수 = 메소드
    # 매개 변수의 목록에 한 개의 변수가 추가
    # 이 변수는 파이썬이 자동으로 값을 할당
    # 현재 객체 자신의 참조가 할당
    # 일반적으로 self 라 명명
'''
# 단순한 클래스 예시

class Person:               # 1. 클래스의 생성
    pass # An empty block   # 2. 클래스의 블록 시작 (pass:아무일도 하지 말고 지나감) 
                            # 3. 블록
p = Person ()               # 4. 클래스의 객체 생성
print(p)                    # 5. 결과 확인

# 메소드 = 함수와 동일하다 (self 제외)
# 클래스 안 함수(메소드)에 사용되는 self

class Person:
    def say_hi(self):
        print('Hello, how are you?')
p = Person()    # 클래스를 객체에 할당 (인스턴스화 된다 라고 함)
p.say_hi()

# say_hi 메소드는 어떤 값도(매개변수) 받지 않음
# say_hi 메소드는 함수정의에 self 를 매개변수로 가지고 있음 

# init 메소드
    # init 메소드는 클래스가 인스턴스화 될 때 호출
    # 객체가 생성시 초기화 명령이 필요할 때 유용
    # init 의 앞뒤로 밑줄 두개씩 입력

class Person:
    def __init__(self, name):   # 인스턴스화 될 시 자동으로 호출되는 함수
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Baram')
p.say_hi()

# 클래스 변수와 객체 변수
    # 클래스 변수
        # 공유됨
        # 모든 인스턴스들이 접근할 수 있음
        # 한개만 존재함
        # 객체가 값을 변경하면 다른 인스턴스에 적용됨
    # 객체 변수
        # 개별 객체/인스턴스에 속함 (독립)
        # 다른 인스턴스들이 접근할 수 없음
        # self 에 연결 (self.name)

class Robot:
    """Represents a robot, with a name."""
    # A class variable, counting the number of robots
    population = 0          # 클래스 변수

    def __init__(self, name):
        """Initializes the data."""
        self.name = name    # 인스턴스 변수
        print("(Initializing {})".format(self.name))

# 데코레이터 @classmethod
    # 클래스 메소드로 만들어줌
@classmethod
    def how_many(cls):

# 옛날방식 (지금은 사용 안함)
# how_many = classmethod(how_many)
'''

# 1 & 2     메소드
'''
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
'''
# 3         일반 함수
'''
def say_hi():
    print('Hi!')

say_hi()
'''
# 4         일반 함수
'''
def sum_ab(a,b):
    print('a + b = ',a+b)

sum_ab(1,2)
'''
# 5
'''
class Person:
    def __init__(self, name):
        self.n = name    # 클래스 안의 객체 변수 선언, self와 붙어 사용이 된다
    
    def say_hi(self):
        print('Hello, my name is', self.n)

p = Person('Minho')
p.say_hi()
'''
# 6

class Robot:
    """Represents a robot, with a name."""
    population = 0  # class variable, counting the number of robots

    def __init__(self, name):   # __init__은 자동으로 호출이 됨
        """Initializes the data."""
        self.n = name   # instance variable, records the name of itself
        print("(Initializing {})".format(self.n))
        Robot.population += 1 # 객체(로봇)이 만들어지면 population에 +1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.n))
        Robot.population -= 1 # 로봇이 제거되면서 population - 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.n))
        else:
            print("There are still {:d} robot(s) working.".format(Robot.population))
    
    def say_hi(self):
        """Greetings by the robot. Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.n))

    @classmethod        # 데코레이터, 바로 다음에 나오는 함수가 클래스 메소드임
    def how_many(cls):  # cls로 클래스 메소드임을 알림
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")  # __init__ 함수의 name에 R2-D2가 들어감
droid1.say_hi()

Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()

Robot.how_many()

print("\nRobots are working now.\n")
print("Robots have finished work. So let's destroy them.")

droid1.die()
droid2.die()
Robot.how_many()