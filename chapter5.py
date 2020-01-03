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




