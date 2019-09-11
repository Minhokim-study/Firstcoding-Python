#연산순서

#괄호를 사용하여 순서 변경

result = 1+2*3 #곱하기 먼저, 다음 더하기
result = (1+2)*3 #더하기 먼저, 다음 곱하기

#[기본] 왼쪽에서 오른쪽으로
a = 1+2+3
a = (1+2)+3

#[할당] 오른쪽에서 왼쪽으로
#a = b = c

#사각형 두변의 길이를 입력하면 면적과 둘레를 구하는 프로그램을 작성하시오
#이때 두 변은 length, width 변수를 쓰고, 각 5.2와 3.79를 넣어 프로그램을 작성합니다.
#최종 화면은 다음과 같습니다

#면적은 **** 입니다.
#둘레는 **** 입니다.
'''
length = 5.2
width = 3.79

dimension = length * width
perimeter = (length + width) * 2

print('면적은', dimension, '입니다.')
print('둘레는', perimeter, '입니다.')
'''
# input("")
# 입력함수, 문자열로 입력값 처리, 숫자 처리의 경우 int, float와 같이 사용


length = float(input("길이를 입력하세요 :"))
width = float(input("폭을 입력하세요 :"))

dimension = length * width  #2진수의 한계로 10진수와 다른 값이 나옴
perimeter = (length + width) * 2

print('면적은', dimension, '입니다.')
print('둘레는', perimeter, '입니다.')

print(0.1+0.2)  #2진수의 한계로 0.300000000000004가 나옴

a = 0.1 + 0.2
print(a)
print(format(a, '.54f')) #64bits = 1 + 11 + 52, 54번째 자리

# if(a==0.3):
# a 는 0.3이 아님