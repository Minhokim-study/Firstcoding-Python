# 자료구조 - 리스트
# " 리스트, 클래스 (메소드, 필드) append, sort, len
# 파이썬은 문자열을 다루기에 적합한 언어이며, 열거형 자료인 문자열은 보통
# 리스트나 튜플같은 자료구조를 사용하여 처리한다.

# 리스트란?
# 1. 순서대로 정리된 항목들을 담고 있는 자료 구조
# 추가하거나 삭제 가능
# 대괄호 [ ] 로 묶음
# mylist = [1, 2, 'a', 'book', ['one', 'two']]

# 객체와 클래스 간단 소개
# i = 5
# int 라는 클래스의 객체 i를 만든다
# i에 5라는 값을 저장한다

# 클래스 - 만들고 싶은 것을 찍어낼 수 있는 무형의 틀
# 객체 - 클래스로 찍어서 만들어 낸 객체

# 클래스의 속성
# 함수 - 클래스에 정의된 함수 -> 메소드
# 변수 - 클래스에 정의된 변수 -> 필드

# 1. list 클래스로 객체를 만든다.
# 2. 객체 이름을 mylist라 한다
# 3. mylist는 list 클래스의 메소드(함수)를 쓸 수 있다.
# 4. list 클래스에는 append()라는 메소드가 있다.
# 5. mylist.append() 처럼 써서 append()메소드를 사용한다.

shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are: ', end='')
for item in shoplist :
    print(item, end='  ')

print('\nI also have to buy rice.')

shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]

del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
