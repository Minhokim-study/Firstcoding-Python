# while 반복문
# 특정 조건이 True인 경우 블럭안의 명령들을 반복해서 실행
# else 절이 따라올 수 있음 (break 배울때 같이 배울 것임)

# indent 기준으로 block 구분
# while 조건 :
#   명령
# else :
#   명령

'''
반복적으로 사용자가 입력한 숫자가 저장된 수보다 크면
"틀렸습니다. 조금 더 작은수입니다." 를, 작으면
"틀렸습니다. 조금 더 큰 수입니다." 를 출력하고, 같으면
"맞았습니다."를 출력하고 종료하는 프로그램을 만들어 보세요.
'''

#내가 짠 코드
'''
number = 23
user_number = int(input("숫자를 입력하세요: "))

while user_number != 23:
    if user_number < 23:
        print("틀렸습니다. 조금 더 큰 수입니다.")
    else :
        print("틀렸습니다. 조금 더 작은 수입니다.")
    user_number = int(input("다시 숫자를 입력하세요."))
print("정답입니다. 프로그램 종료")
'''

#교재 코드
'''
number = 23
running = True
while running :
    guess = int(input("숫자를 입력하세요 :"))
    if guess == number :
        print('맞았습니다.')
        running = False
    elif guess < number :
        print("틀렸습니다. 조금 더 큰 수입니다.")
    else :
        print("틀렸습니다. 조금 더 작은수입니다.")
print("프로그램 종료")
'''

'''
사용자가 입력한 숫자가 짝수이면, '짝수입니다.'를 출력하고, 
3의 배수이면. '3의 배수입니다.'를 한줄에 출력하는 프로그램을 만들어 보세요.
단, 777을 입력하면 종료하고, 나머지 수에 대해서는 프로그램 실행을 반복합니다.
'''

#내가 짠 코드
'''
running = True
while running :
    guess = int(input("숫자를 입력하세요: "))

    if guess % 6 == 0:
        print("2와 3의 배수입니다.")
    elif guess % 2 == 0:
        print("2의 배수입니다.")
    elif guess == 777:
        print("3의 배수이지만, 프로그램을 종료합니다.")
        running = False
    elif guess % 3 == 0:
        print("3의 배수입니다.")
'''

#교재 코드
running = True
while running:
    guess = int(input("숫자를 입력하세요: "))
    if guess % 2 == 0 and guess % 3 == 0 :
        print(guess, "는 짝수이면서, 3의 배수입니다.")
    else:
        if guess % 2 == 0 :
            print (guess, "는 짝수입니다.")
        if guess % 3 == 0 :
            print (guess, "는 3의 배수입니다.")
        if guess == 777 :
            running = False
print ("프로그램 종료.")