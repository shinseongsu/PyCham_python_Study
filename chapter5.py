# 클래스

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))


result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


# 클래스 맛보기

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2)

print(a.first)
print(a.second)

a = FourCal()
b = FourCal()

a.setdata(4, 2)
print(a.first)

b.setdata(3, 7)
print(b.first)

# 주소 알아보기

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(id(a.first))
print(id(b.first))

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(2, 4)

print(a.add())

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())


# 생성자

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a = FourCal(4, 2)
print(a.first)
print(a.second)

# 클래스 상속

class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())

# 메서드 오버라이딩

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())


# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"

print(a.lastname)
print(b.lastname)

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))


# 모듈

import mod1
print(mod1.add(3,4))
print(mod1.sub(4,2))

from mod1 import add
print(add(3, 4))

from mod1 import add, sub
from mod1 import *

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

print(mod2.add(mod2.PI, 4.4))

# 패키지

import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

#relative 패키지

from game.graphic.render import render_test
render_test()



# 예외 처리

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

try:
    a = [ 1, 2 ]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")



try:
    a = [ 1, 2 ]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 오류 회피하기

try:
    f = open("나없는 파일", 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
#eagle.fly() 에러 발


class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


# 예외 만들기

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

say_nick("천사")
# say_nick("바보")

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않은 별명입니다.")


# 내장 함수

print(abs(3))
print(abs(-3))
print(abs(-1.2))


print(all([1,2,3]))
print(all([1,2,3,0]))


print(any([1, 2, 3, 0]))
print(any(["", 0]))


print(chr(97))
print(chr(48))


print(dir([1,2,3]))
print(dir({'1':'a'}))


print(divmod(7, 3)) # (몫, 나머지)

print(7 // 3)       # 몫
print(7 % 3)        # 나머지


for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))


# filter

def position(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(position([1, -3, 2, 0, -5, 6]))


def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 3])))

print(hex(234))
print(hex(3))

a = 3
print(id(3))
print(id(3))
b = a
print(id(b))

print(id(4))

a = input()
print(a)
b = input("Enter: ")
print(b)


print('3')
print(3.4)


print(int('11', 2))
print(int('1A', 16))


class Person: pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))


print(len("python"))
print(len([1,2,3]))
print(len((1, 'a')))


print(list("python"))
print(list((1,2,3)))


a = [1, 2, 3]
b = list(a)
print(b)

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)


def two_times(x): return x*2

print(list(map(two_times, [1, 2, 3, 4])))

print(list(map(lambda a: a*2, [1, 2, 3, 4])))


print(max([1, 2, 3]))
print(max("python"))

print(min([1, 2, 3]))
print(min("python"))

# 8 진수
print(oct(34))
print(oct(12345))


# 아스키 코드
print(ord('a'))
print(ord('0'))

print(pow(2,4))
print(pow(3,3))


print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))


print(round(4.6))
print(round(4.2))
print(round(5.678, 2))


print(sorted([3,1,2]))
print(sorted((['a', 'c', 'b'])))
print(sorted("zero"))
print(sorted((3,2,1)))


print(str(3))
print(str('hi'))
print(str('hi'.upper()))


print(sum([1,2,3]))
print(sum((4,5,6)))


print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1,2,3)))


print(type("abc"))
print(type([]))


print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))
print(list(zip("abc", "def")))


#sys

import sys
print(sys.path)

# os

import os
print(os.environ)       #  시스템 정보
print(os.getcwd())      #  디렉터리 위치 돌려받기
print(os.system("dir")) #  시스템 명령어 호출

f = os.popen("dir")
print(f.read())


# time


import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())


print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))


for i in range(10):
    print(i)
    time.sleep(1)


# calendar

import calendar
print(calendar.calendar(2015))
print(calendar.prcal(2015))
print(calendar.prmonth(2015, 12))
print(calendar.weekday(2015, 12 ,31))
print(calendar.monthrange(2015, 12))     # 1일이 무슨요일인지, 며칠까지 있는지

# random

import random
print(random.random())              # 0.0 ~ 1.0 사이 래덤
print(random.randint(1, 10))         # 1에서 10 사이 랜덤
print(random.randint(1, 55))


import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

import webbrowser
webbrowser.open("http://google.com")

webbrowser.open_new("http://google.com")





