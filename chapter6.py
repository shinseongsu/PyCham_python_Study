#  구구단

def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

print(GuGu(2))


# 3과 5의 배수 합하기

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n

print(result)

# 게시판 페이징

def getTotalPage(m,n):
    return m // n + 1

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))


# 간단한 메모장 만들기

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()


# 탭을 4개의 공백으로 바꾸기

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()
space_content = tab_content.replace("\t", " " * 4)

f = open(dst, 'w')
f.write(space_content)
f.close()


# 하위 디레토리 확인

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("/Users/mac/Desktop/Python")
