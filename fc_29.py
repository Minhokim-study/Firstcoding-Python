# 파일 입출력
# " palindrome, open(), close(), write(), pickle
# palindrome = 뒤집힌 문자열과 원래의 문자열이 일치하는 것
# 슬라이스 사용 : 문자열 뒤집기

# 문장부호, 공백 등을 포함한 문자열의 palindrome을 검사할 수 있는 프로그램으로 개선할 것
# ex. "Rise to vote, sir."

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter Text: ")
while something == "":
    something = input("Enter more than one character: ")
something = something.lower()
something_list = list(something)
print(something_list)
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
palindrome_check = []


for i in something_list:
    if i in abc:
        palindrome_check.append(i)

check_str = ''.join(palindrome_check)
print(check_str)

if is_palindrome(check_str):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
