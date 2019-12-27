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

