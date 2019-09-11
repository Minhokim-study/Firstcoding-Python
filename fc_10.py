# for .. in 문
# 일정 회수를 정한 상태에서 반복문을 사용하고자 할 때 편리하다.

# 열거형 데이터에 포함된 각 항목을 하나씩 거쳐가며 실행
# 열거형: 여러 항목이 나열된 어떤 목록

for i in range (1,5) :
    print (i)       # i 는 list 형, [1,2,3,4]
print ("for 문이 종료되었습니다.")

### range (시작, 끝, 증감) ###
# 시작: 지정되지 않으면 기본값 0
# 끝: 포함되지 않음
# 증감: 지정되지 않으면 기본값 1
# 정수 (음수포함)만 사용

'''
for 문을 이용해서 구구단을 출력하는 프로그램을 만들어 보세요
'''

#내가 한 코딩
'''
for gugu_number1 in range (1,10) :
    for gugu_number2 in range (1,10) :
        print (gugu_number1," x ", gugu_number2, " = ", gugu_number1 * gugu_number2)
print ("구구단이 종료되었습니다.")
'''

#교재 코딩
for firstNumber in range (2,10) :
    print(firstNumber, "단")
    for secondNumber in range (1,10) :
        print(firstNumber, "*", secondNumber, "=", firstNumber*secondNumber)
print("프로그램 종료.")