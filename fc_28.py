# 상속
# 클래스는 코드 재활용을 위하여 좋은 방법을 제공 함 -> 상속을 잘 활용할 것

# 객체지향의 장점 = 코드재활용 = 상속
# 클래스간의 크고 작은 형식을 구현

# 교수와 학생들의 명부 작성 프로그램
    # 교수 & 학생 : 이름, 나이, 주소
    # '교수' 만 : 연봉, 과목, 휴가
    # '학생' 만 : 성적, 등록금

# 방법 1 : 2개의 클래스
    # 교수 - 이름, 나이, 주소, 연봉, 과목, 휴가
    # 학생 - 이름, 나이, 주소, 성적, 등록금

# 방법 2 : 공통 클래스와 상속
    # 공통클래스 (SchoolMember) - 이름, 나이, 주소      //슈퍼클래스, 부모클래스
    # 교수 (Teacher) - 연봉, 과목, 휴가 + 공통클래스    //서브클래스, 자식클래스
    # 학생 (Student) - 성적, 등록금 + 공통클래스        //서브클래스, 자식클래스

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name: {} Age: {}'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
        print('(Initialized Student: {})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Score: {:d}'.format(self.score))

t = []
t.append(Teacher('촘스키', 50, 32500))
t.append(Teacher('개놈스키', 44, 35500))
t.append(Teacher('썅놈스키', 35, 42500))
t.append(Teacher('캐스키', 40, 52500))
s = []
s.append(Student('싸이', 25, 65))
s.append(Student('홍길동', 45, 55))
s.append(Student('민호', 35, 100))

print()
members = t + s
for member in members:
    member.tell()