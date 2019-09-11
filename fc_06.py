#할당연산자
'''
a = 2
print(a)
a = a * 3   #이방식 추천
print(a)
a *= 3
print(a)

a = a + 1   #이방식 추천
print(a)
a += 1
print(a)

a = 2

a += 3
print(a)
a -= 3
print(a)
a *= 3
print(a)
a /= 3
print(a)

a = 2
a **= 3
print(a)
'''
#복소수 : 제곱을 했을 때 -1이 되는 수

j = 2
j = j
j = 2j
j = 2*j
print(j)

a = 1 - 2j          # 1 - 2j
b = complex(1,2)    # 1 + 2j 위아래 두개의 켤레복소수
print(a+b)          # 2
print(b-a)          # 4j
print(a*b)          #(1-2j)(1+2j) = (1 + 4) = 5

print(a.real)           #실수부
print(a.imag)           #허수부
print(a.conjugate())    #켤레복소수
print(abs(a))                  #크기

'''변화된 내용'''