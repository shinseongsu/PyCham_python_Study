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


