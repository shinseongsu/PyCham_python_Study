# if 문 구조

money = True

if money:
    print("택시를")
    print("타고")
    print("가라")

x = 3
y = 2
print(x > y)


money = 3000;
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")


money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고가라")
else:
    print("걸어가라")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ['a', 'b', 'c'])
print('j' in 'python')

poket = ['paper', 'cellphone', 'money']
if 'money' in poket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# while문

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())


coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 1
while True:
    money = int(input("돈을 넣어 주세요:"))
    if money == 300:
        print("커피를 숩니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다."% coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

# 무한 루프
#while True:
#    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

# for문

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)


a = range(10)
print(a)        # 0 ~ 9

a = range(1, 11)
print(a)        # 1 ~ 11

add = 0
for i in range(1, 11):
    add = add + i

print(add)


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다."% (number+1))


for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print(' ')


a  = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x * y for x in range(2, 10)
    for y in range(1,10)]
print(result)


###################
#   연습문제 #
###################

# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

result = 0
i = 1
while i <= 1000:
    if (i % 3) == 0:
        result += i
    i += 1

print(result)


# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)


# for문을 사용해 1부터 100까지의 숫자를 출력해보자.
for i in range(1, 101):
    print(i)


# A학급에 총 10명의 하갱이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 85, 100]

A = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

# 리스트 중 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

# numbers = [1,2,3,4,5]
# result = []
# for n in numbers:
#   if n % 2 == 1:
#       result.append(n*2)

numbers = [1,2,3,4,5]
result = [ n * 2 for n in numbers]
print(result)



