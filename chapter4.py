# 함수

def add(a, b):
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)

print(add(a,b))

def add(a, b):
    result = a + b
    return result

a = add(3,4)
print(a)

# 매개변수 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

# 결과값 없는 함수
def add(a,b):
    print("%d %d의 합은 %d입니다." % (a, b, a+b))

add(3, 4)

a = add(3,4)
print(a)

# 매개변수도 없고 결괏값도 없는 함수
def say():
    print('Hi')

say()


# 매개변수 지정하여 호출하기

def add(a, b):
    return a + b

result = add(a=3, b=7)
print(result)

result = add(b=5, a=3)
print(result)

# 여러개의 입력값을 받는 함수 만들기

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# 함수의 결괏값은 언제나 하나이다
def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)


# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박응용", 27)
say_myself("박응용", 27, True)

a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

def vartest(a):
    a = a + 1

vartest(3)
print(a)


a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)


# global 명령어 사용하기

a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)


add = lambda a, b: a+b
result = add(3, 4)
print(result)

def add(a, b):
    return a + b

result = add(3,4)
print(result)


# 사용자 입력

a = input()
print(a)

number = input("숫자를 입력하세요.")
print(number)

a = 123
print(a)

a = "python"
print(a)

a = [ 1, 2, 3 ]
print(a)

print("life" "is" "too short")
print("life" + "is" + "too short")

print("life", "is", "too short")

for i in range(10):
    print(i, end = ' ')







