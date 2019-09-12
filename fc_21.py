# 자료구조 - 튜플
# 1. 여러 객체를 모아 담는데 사용 (리스트와 동일)
# 2. 수정 불가 (리스트는 수정 가능)
# 3. 튜플은 생략할 수 있는 괄호로 묶고, 쉼표로 구분된 여러개의 항목으로 정의
# ex1) zoo = ('python', 'elephant', 'penguin')
# ex2) zoo = 'python', 'elephant', 'penguin'

zoo = ('python', 'elephant', 'penguin')
print('동물원에 있는 동물의 수 : ', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('새 동물원에 있는 우리의 수 : ', len(new_zoo))
print('새 동물원에 있는 동물들 : ', new_zoo)
print('옛 동물원에서 온 동물들: ', new_zoo[2])
print('옛 동물원에서 온 마지막 동물:', new_zoo[2][2])
print('새 동물원의 동물 수 : ', len(new_zoo)-1+len(new_zoo[2]))

# new_zoo = ('monkey', 'camel', ('python', 'elephant', 'penguin'))
# new_zoo 의 세번째 항목 : new_zoo[2]
# new_zoo[2] 는 튜플이며, 이것의 세번째 항목은 new_zoo[2][2]

# 빈 튜플 만드는법은 myempty = ()
# 항목을 1개만 담는 튜플, singleton = (2,) #콤마 꼭 써줄것
#   NOT singleton = (2) # 2라는 정수형 값에 대하여 앞뒤에 괄호를 쳐 준 것으로 인식
