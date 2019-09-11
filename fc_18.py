# 모듈만들기
# "__main__, __version__, import *, import this

# 모든 모듈은 이름을 가지고 있음
# 모듈 내 포함된 명령으로 모듈의 이름 확인
# 실행되었을때 : __main__
# import 되었을 때 : 모듈의 이름

if __name__ == '__main__' :
    print('I am running. My name is ', end='') # end=''로 줄바꿈 방지
    print(__name__)

else :
    print("I'm imported. My name is ", end='' )
    print(__name__)

# import this    "ZEN of Python"