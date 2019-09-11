# dir 내장함수
# 객체(모듈)에 정의된 식별자(이름) 불러오기
# 모듈은 함수, 클래스, 변수를 가지고 있음
# dir()은 모듈에 포함된 식별자 목록을 반환

'''
import sys
for num in dir(sys):
    print(num)
'''
'''
import sys
a = 100
dir() 시 목록에 a가 추가됨
del a
dir() 시 나오는 목록에 a가 제거됨
'''