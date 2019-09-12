# 자료구조 - 사전
# 세번째 열거형 자료구조 (리스트, 튜플에 이어)
# Key 와 Value가 쌍으로 묶여있는 구조
# Key : 정적 객체 (이름에 해당)
# Value : 정적, 비정적 객체 모두 (주소나 연락처에 해당)
# d = {key1:value1, key2:value2}
    # Key 와 Value는 콜론으로 구분 (:)
    # 각 쌍은 쉼표로 구분 (,)
    # 전체는 중괄호 {} 로 묶음
'''
ab = { '홍길동' : '000-0000', '철수' : '990-0099', '영희' : '453-3939'}
'''

# 'ab' is short for 'a'ddress 'b'ook
ab = {  'Baram' : 'ludenscode@gmail.com',
        'Larry' : 'larry@wall.org',
        'Oyamada' : 'Oyamada@aktsk.com',
        'Helen' : 'helen19930608@yahoo.com.tw'
}
print("Baram's address is", ab['Baram'])

# Deleting a key-value pair
del ab['Oyamada']
print('\nThere are {} contacts in the address book\n'.format(len(ab)))

for name in ab:
    print(name)

for name in ab:
    print(name, ab[name])
    
for name, address in ab.items():
    print('Contact {} at {}' .format(name, address))

# Adding a key-value pair
ab['Gildong'] = 'gildong@abuzi.org'

if 'Gildong' in ab:
    print("\nGildong's address is", ab['Gildong'])