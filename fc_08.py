#if 조건문
#조건에 따라 정해진 명령을 실행

'''
if 조건문을 사용해서 사용자가 입력한 숫자가 파이썬에 저장된 수보다 크면
"틀렸습니다. 조금 더 작은 수입니다."를, 작으면 "틀렸습니다. 조금 더 큰
수입니다."를, 같으면 "맞았습니다."를 출력하는 프로그램을 만들어 보세요.
'''
#if, elif, else 사용/ input()함수 사용/ print()함수 사용
#비교연산자 ==, <, > 사용/ 대입연산자 = 사용/ 변수 사용/ 비교할 값은 23
'''
guess = 23
user_guess = int(input("파이썬이 생각하는 숫자를 맞춰 보세요 (1~100): "))

if user_guess > guess :
    print("틀렸습니다. 조금 더 작은 수입니다.")
elif user_guess < guess :
    print("틀렸습니다. 조금 더 큰 수입니다.")
else :
    print("맞았습니다.")

print("프로그램 종료")
'''
#if 문
'''
if 조건 :
    명령
elif 조건 :
    명령
else :
    명령

4칸 띄워쓰기 (indent)
콜론 : 은 새로은 블럭의 시작
elif / else 블럭은 생략 가능
'''

#input()함수
'''
input("화면에 표시할 내용")
input 함수의 결과값은 문자열 (string)
문자열을 정수로 변환
int(문자열) 

name = input("이름을 입력하세요: ")
number = int(input("수를 입력하세요: "))
'''

'''
if 조건문을 사용해서 사용자가 입력한 숫자가 짝수이면 "짝수입니다."를 출력하고,
3의 배수이면 "3의 배수입니다."를 출력하는 프로그램을 만들어보세요.
'''
# if 조건문 사용 / input()함수 사용 / print() 함수 사용 / 나머지 연산자 % 사용
# 대입연산자 = 사용 / 변수 사용

'''내가 짠 프로그램
user_input = int(input("숫자를 입력하세요: "))

if user_input % 2 == 0 :
    print("짝수입니다.")
    if user_input % 3 == 0 :
        print("3의 배수입니다.")
elif user_input % 3 == 0 :
    print("3의 배수입니다.")
else :
    print("2나 3의 배수가 아닙니다.")

print("프로그램 종료")
'''

guess = int(input("숫자를 입력하세요: "))
if guess % 2 == 0:
    print(guess, "는 짝수입니다.")

if guess % 3 == 0:
    print(guess, "는 3의 배수입니다.")

print("프로그램 종료")