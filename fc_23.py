# 열거형과 슬라이스연산

# 멤버쉽 테스트
    # in / not in
    # 인덱싱 연산
        #슬라이스 연산 - 일부분을 잘라냄

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'sleep'

# Indexing or 'Subscription' operation #
print('Item 2 is', shoplist[2])
print('Item 0 is', shoplist[0])
print('Item 3 is', shoplist[3])
print('Item 1 is', shoplist[1])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

print('')

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3]) # 1번 항목에서 3번 항목 전까지 ['mango', 'carrot']
print('Item 2 to end is', shoplist[2:]) # 2번 항목 (세번째 항목)에서 끝까지
print('Item 1 to -1 is', shoplist[1:-1]) # 1번 항목에서 -1번째 항목 (마지막 항목) 전까지
print('Item start to end is', shoplist[:]) # 처음 항목에서 마지막 항목까지

print('')

# Stepping on a list #
print('Item start to end with step 1 is ', shoplist[::1]) # 세번째 인수는 스텝을 의미
print('Item start to end with step 2 is ',shoplist[::2]) # 전체를 포함하는데, 두개씩 띄움
print('Item start to end with step -1 is ',shoplist[::-1]) #열거형의 순서를 역순으로 바꿀때 스텝에 -1을 사용

print('')

mylist = [str(1),2,3,4,5,]

if 1 in mylist:   #str 인지 int 인지 항상 주의할것
    print("1-OK")

if 1 not in mylist:
    print("1-NOT OK")