# 참조
# 객체 생성 -> 변수에 할당
# 변수에 객체의 참조가 할당

shoplist = ['apple', 'mango', 'carrot', 'banana']   # shoplist는 메모리상 리스트 자료 주소를 참조

mylist = shoplist                                   # mylist 는 shoplist 를 참조, 컴퓨터 메모리에 큰 영향 없음

del shoplist[0]
print('shoplist is ', shoplist)
print('mylist is ', mylist)


mylist = shoplist[:]                                # shoplist의 리스트 자료를 복사해서 mylist에 집어 넣음

print('shoplist is ', shoplist)                     
print('mylist is ', mylist)
del mylist[0]
print('modified shoplist is ', shoplist)
print('modified mylist is ', mylist)
# 변수 = 객체이름
    # mylist = shoplist
    # 주소값이 전송 / 같은 곳을 가리킴
# 변수 = 슬라이스연산자(객체)
    # mylist = shoplist[:]
    # 값을 복사하여 전송 / 새로운 객체 생성

