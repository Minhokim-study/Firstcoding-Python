# 모듈 이해
# "from, import, argv...

# 모듈이란: 여러 함수를 한꺼번에 불러들여 재사용

# .py 확장자를 가진 파일안에 함수와 변수를 정의
# 파이썬 인터프리터를 만든 언어로 모듈 작성 (ex. C언어)

# import 명령으로 모듈을 불러와 사용
'''

import sys
...
for i in sys.argv:
...

'''
'''
import sys

print("The command line arguments are: ")
print(sys.argv)
for i in sys.argv:
    print(i)
print("\n\nPATH is")
for i in sys.path:
    print(i)

#or
'''
from sys import argv, path

print("The command line arguments are: ")
print(argv)
for i in argv:
    print(i)
print("\n\nPATH is")
for i in path:
    print(i)

# 바이트 컴파일된 .pyc
# .pyc는 바이트 컴파일 중간 단계의 파일로 .py 파일이 저장된 곳에 생성
# 선행작업을 통해 .pyc 생성, 속도 향상을 가져옴


# from ... import 문
# sys.argv 대신 argv 사용할 때
# from sys import argv 구문 사용
'''
from math import sqrt
print("Square root of 16 is", sqrt(16))
help(sys)
'''