# 아래 프로그램은 사용자로부터 이름과 나이를 입력 받아서 출력하는 프로그램입니다.
# 샾 기호의 단축키는 ctrl + /

name = input("이름을 입력하세요. : ")
age = input("나이를 입력하세요. : ")

print("안녕하세요, " + name + "님. 만나서 반갑습니다. 입력하신 나이는 " + age + " 입니다.")
print(f"안녕하세요, {name}님. {name}님의 나이는 {age} 입니다.")
if age < 18:
    print("나이 제한으로 인한 회원가입이 불가합니다.")