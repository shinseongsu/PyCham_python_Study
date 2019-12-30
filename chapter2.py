# 정수형

a = 123
a = -178
a = 0

# 실수형

a = 1.2
a = -3.45

a = 4.24E10
a = 4.2e-10

# 8진수와 16진수
a = 0o177

a = 0x8ff
b = 0xABC

# 사칙연산

a = 3
b = 4
print( a + b )
print( a * b )
print( a / b )

# x의 y제곱을 나타내는 **연산자

a = 3
b = 4
print(a ** b)

# 나눗셈 후 나머지를 반환하는 % 연산자

print( 7 % 3 )
print( 3 % 7 )

# 나눗셈 후 몫을 반환하는 // 연산자

print( 7 / 4 )
# 나눗셈 후 몫을 반
print( 7 // 4 )



# 큰따옴표(")로 양쪽 둘러싸기
print("Hello World")

# 작은따옴표(')로 양쪽 돌러싸기
print('Python is fun')

# 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")

# 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')


# 문자열에 작은따옴표(') 포함시키기
food = "Python's favorite food is perl"

print(food)

# 문자열에 큰따옴표(") 포함시키기
say = '"Python is very easy." he says.'

print(say)


# 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food)
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 떄

multiline = "Life is too short\nYou need python"
print(multiline)


# 연속된 작은 따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기

multiline = '''
    Life is too short
    You need python
'''
print(multiline)
multiline = """
    Life is too short
    You need python
"""
print(multiline)


# 문자열 더해서 연결하기

head = "Python"
tail = " is fun!"
print(head + tail)

# 문자열 곱하기
a = "python"
print ( a * 2 )

# 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))


# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])

# 문자열 슬라이딩

print(a[-2])
print(a[-5])

print (a[0:4])
print(a[19:])

print(a[:17])
print(a[:])
print(a[19:-7])

# 슬라이싱으로 문자열 나누기

a = "20010331Rainy"
date = a[:8]
weather = a[8:]

print(date)
print(weather)

year = a[:4]
day = a[4:8]
weather = a[8:]

print(year)
print(day)
print(weather)

a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])


# 문자열 포맷팅

print("I eat %d apples." %3)

print("I eat %s apples. " %"five")

number = 3
print("I eat %d apples" %number)


# 2개 이상의 값 넣기

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day))

print("I have %s apples" % 3)
print("rate is %s" % 3.234)

print("%10s" % "hi")

print("%-10sjane" % 'hi')

# 소수점 표현하기

print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

# format 함수를 사용한 포맷팅

print("I eat {0} apples".format(3))

print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples".format(number))

number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days".format(number, day))


print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days".format(10, day=3))

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print("{0:0.4f}".format(3.42134234))

print("{{ and }}".format())

# f 문자열 포매팅
name = '홍길동'
age =30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 39
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name' : '홍길동', 'age': 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')

print(f'{"hi":!<10}')
print(f'{"hi":=^10}')

y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')

print(f'{{and}}')

a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

a = "Life is too short"
print(a.index('t'))

print(",".join('abcd'))
print(",".join(['a','b','c','d']))

a = "hi"
print(a.upper())

a = " hi "
print(a.lstrip())
print(a.rstrip())

a = " hi "
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(":"))


# 리스트 자료형

a = [1,2,3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1])
print(a[3])
print(a[-1][0])

# 리스트의 슬라이싱

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = "12345"
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]

print(b)
print(c)


# 리스트 연산하기

a = [1,2,3]
b = [4,5,6]

print(a + b)

# 리스트 반복하기
a = [1, 2, 3]
print(a * 3)

# 리스트 길이 구하기
print(len(a))


# 리스트에서 값 수정하기

a = [1,2,3]
a[2] = 4
print(a)

# del 함수로 리스트 요소 삭제하기
a = [1, 2,3]
del a[1]
print(a)


a = [1, 2, 3, 4, 5]
del a[2:]
print(a)


# 리스트에 요소 추가

a = [1,2,3]
a.append(4)
print(a)

a.append(([5,6]))
print(a)

a = [1,4,3,2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)


# 리스트 뒤집기

a = ['a', 'c', 'b']
a.reverse()
print(a)

# 위치 반환

a = [1, 2, 3]
print(a.index(3))
print(a.index(1))


# 리스트에 요소 삽입

a = [1,2,3]
a.insert(0, 4)
print(a)

a.insert(3,5)
print(a)

# 리스트 제거(remove)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

#리스트 요소 끄집어내기

a = [1, 2, 3]
print(a.pop())
print(a)

a = [1,2,3]
print(a.pop(1))

# 리스트에 포함된 요소 x의 개수 세기(count)

a = [ 1, 2, 3, 1]
print(a.count(1))

a  = [1,2,3]
a.extend([4,5])
print(a)

b = [6,7]
a.extend(b)
print(a)


# 튜플

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

t1 = (1, 2, 'a', 'b')
print(t1[1:])

t2 = (3, 4)
print(t1 + t2)

print(t2 * 3)

t1 = (1, 2, 'a', 'b')
print(len(t1))


#딕셔너리

a= {1: 'a'}
a[2] = 'b'
print(a)

del a[1]
print(a)

a = {1: 'a', 2: 'b'}
a['name'] = 'pey'
print(a)

a[3] = [1,2,3]
print(a)

del a[1]
print(a)

grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

dic = {'name': 'pey', 'phone':'0119993323', 'birth':'1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

a = {1:'a', 1:'b'}
print(a)

# 딕셔너리 관련 함수

a = { 'name' : 'pey', 'phone' : '0119993323' }
print(a.keys())

print(list(a.keys()))

print(a.values())

print(a.items())

a.clear()
print(a)

a = {'name':'pey', 'phone': '0119993323', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))

print(a.get('foo', 'bar')) # 맨 뒤쪽은 디폴트값 키 없으면 뒤에 꺼

a = {'name' : 'pey', 'phone': '0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)

# 집합 자료형

s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2)

# 자료형 특징
# 중복을 허용하지 않는다.
# 순서가 없다.

s1 = set([1,2,3])
l1 = list(s1)

print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

# 교집합, 합집합, 차집합 구하기

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print( s1 & s2)

print(s1.intersection(s2))

#합집합

print( s1 | s2)

print(s1.union(s2))

# 차집합

print(s1 - s2)
print(s2 - s1)

print(s1.difference(s2))
print(s2.difference(s1))

# 집합 자료형 관련 함수

s1 = set([1, 2, 3])
s1.add(4)
print(s1)


s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

s1 = set([1,2,3])
s1.remove(2)
print(s1)

# 불 자료형

a= True
b= False

print(type(a))
print(type(b))

print( 1 == 1 )
print( 2 > 1 )
print( 2 < 1 )

# 볼 연산

print(bool('python'))
print(bool(''))

# 변수란?

a = 1
b = "python"
c = [1,2,3]

a = [1,2,3]

print(id(a))    # 메모리의 주소


a = [1, 2, 3]
b = a

print(id(a))    # 복사한건 메모리 같음
print(id(b))

print( a is b)

a[1] = 4
print(a)
print(b)    # b는 안바꿨는데 변경됨

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)    # 슬라이싱 한건 변하지 않음.

from copy import copy
a = [1, 2, 3]
b = copy(a)

print(a)
print(b)
print(a is b)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')

(a, b) = 'python', 'life'

[a,b] = ['python', 'life']

a = b = 'python'


a = 3
b = 5
a, b = b, a
print(a)
print(b)



###################
#   연습문제 #
###################


# 홍길동 씨 의 평균 점수를 구해보자
# 국어 - 80점 , 영어 - 75점, 수학 - 55점

list = [80, 75, 55]
list_len = len(list)
list_sum = list[0] + list[1] + list[2]
result = list_sum / list_len

print('홍길동씨의 평균점수는 : %d' % result)


# 자연수 13이 홀수 인지 짝수인지 판별할 수 있는 방법

count = 13

result = ['짝수', '홀수']
result = result[count%2]

print(f'자연수 13는 {result}입니다.')

# 홍길동씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

pin = "881120-1068234"

yyyymmdd = "19" + pin[:6]

num = pin[7:]

print(yyyymmdd)
print(num)

# 주민등록 번호 뒷자리의 맨 첫번째 숫자는 성별을 나타낸다. 주민등록번호에는 성별을 나타내는 숫자를 출력해 보자.

pin = "881120-1068234"

print(pin[pin.index('-')+1:pin.index('-')+2])


# 다음과 같은 문자열 a:b:c:d 가 있다. 문자열의 replace함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# [1,3,5,,4,2] 리스트를 [5,4,3,2,1] 로 만들어 보자.
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
a = (1,2,3)
a = a + (4,)

print(a)

# 딕셔너리 a에서 'B'에서 해당되는 값을 추출해 보자
a = {'A': 90, 'B': 80, 'C': 70 }
result =  a.get('B')
print(a)
print(result)

# a 리스트에서 중복 숫자를 제거해 보자.

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
print(aSet)