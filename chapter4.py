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

# 파일 생성하기

f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")


# 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해 보자.
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(1))
print(is_odd(2))


# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자.

def avg_number(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_number(1,2))
print(avg_number(1,2,3,4,5))


# 다음 숫자를 입력받아 더하여 돌려주는 프로그램.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." % total)

# 사용자의 입력을 파일에 저장하는 프로그램을 작성해보자.(기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

user_input = input("저장할 내용을 입력하세요:")
f = open('text.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()

# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어서 저장해 보자.

# Life is too short
# you need java

f = open('test2.txt', 'w')
body = """
    Life is too short
    you need java
"""
f.close()

body = body.replace("java", "python")

f = open('test2.txt', 'w')
f.write(body)
f.close()
