# break, continue
# " while, for + else

# break 문은 loop을 강제로 빠져나올 때 사용
#    루프 조건이 'False'가 되지 않았거나
#   열거형의 끝까지 루프가 도달하지 않았지만
#   루프 문의 실행을 강제로 정지시키고 싶을 때 사용
# break 실행시 else 블록은 실행되지 않음
'''
while (조건1) :
    반복내용
    if (조건2) :
        break
else:
    (조건1이 거짓일 때) 실행 할 명령
    실행할 명령
'''
'''
number = 23
running = True
loopState = False

while running :
    guess = int(input("숫자를 입력하세요 :"))
    if guess == 8211 :
        print('종료합니다.')
        break

    if guess == number :
        print('맞았습니다.')
        running = False

    elif guess < number :
        print("틀렸습니다. 조금 더 큰 수입니다.")

    else :
        print("틀렸습니다. 조금 더 작은수입니다.")

else :
    print ("반복문이 정상적으로 종료되었습니다.")
    loopState = True

if loopState == True :
    print('프로그램 정상종료')
else :
    print("프로그램이 강제로 종료되었습니다.")
'''

# continue 문은 현재 실행중인 루프 블록의 나머지 명령문들을 실행하지 않고
# 곧바로 다음 루프로 넘어간다.

while True :
    name = input ("영어 이름을 입력하세요. :")
    if name == "quit" :
        break

    if len(name) < 3 :
        print('너무 작습니다. 다시 입력해주세요')
        continue

    print ("이름을 입력하셨습니다.")