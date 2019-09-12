# 문자열 보충

# 파이썬의 모든 문자열은 str 클래스의 객체
# help(str)

name = 'Minho'
if name.startswith('Min'):
    print('Yes, the string starts with "Min"')
if 'a' not in name:
    print('No, it does not contain the string "a"')
if name.find('inh') != -1: # 'inh' 이라는 값이 없으면 -1이 됨
    print('Yes, it contains the string "inh"')

delimiter = '_*_'
mylist = ['Brazin', 'Russia', 'India', 'China'] # 'Brazin_*_Russia_*_India_*_China'
print(delimiter.join(mylist))                   # join 메소드

for nation in mylist:                           # join 을 모를시
    print(nation, end='')
    if nation != mylist[-1]:
        print(delimiter, end='')
print('')


str1 = "This is an amazing movie!!!"
str2 = "i"

print(str1.find('i', 23))
'''
startnumber = 0
while (startnumber != -1):
    startnumber = str1.find(str2, startnumber)
    print(startnumber)
    if startnumber != -1:
        startnumber = startnumber + 1
count 함수를 모른다면 이런식으로 프로그램을 짤 수 있음
'''
print(str1.count(str2))


        

