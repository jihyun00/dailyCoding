"""
list에 적용할 수 있는 함수들
count는 list 안에 있는 대상의 갯수 출력
a.count('x')는 값이 없으므로 0 출력
insert(a, b)는 리스트의 a의 위치에 b 값 추가
append 함수는 리스트의 맨 뒤에 추가
index(a) 함수는 리스트의 a의 위치 출력
아래 예제의 경우 333이 1번째, 2번째 두 개가 존재.
하지만 리스트의 제일 앞에 있는 인덱스 값 리턴
remove(a) 함수는 리스트에 있는 값 제거
같은 값이 여러 개 있을 경우 리스트의 앞에 있는 값 제거
reverse는 리스트에 있는 내용을 뒤집는다
sort 함수는 리스트에 있는 값 오름차순으로 정렬
pop 함수는 리스트의 맨 뒤에 있는 값 제거
"""
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
a.index(333)
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
a.pop()
print(a)


"""
list를 stack으로 사용 가능
stack의 push 역할을 append 함수로,
stack의 pop 역할을 pop 함수로 사용
"""
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()


"""
list를 queue로도 사용 가능
from collections import deque 호출해서 queue 사용 가능
append는 queue에 pus, popleft는 리스트의 맨 앞에 값 제거
"""
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print(queue)


"""
# TODO
"""
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)


"""
# TODO
"""
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]
freshfruit = ['  banana', '  loganberry ', 'passion fruit   ']
[weapon.strip() for weapon in freshfruit]
print(freshfruit)
# [(x, x**2) for x in range(6)]
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]


"""
# TODO
"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)


"""
# TODO
"""
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


"""
# TODO
"""
print(list(zip(*matrix)))


b = [-1, 1, 66.25, 333, 333, 1234.5]
del b[0]
print(b)

del b[2:4]
print(b)

del b[:]
print(b)


"""
# TODO
"""
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

#t[0] = 88888

v = ([1, 2, 3], [3, 2, 1])
print(v)


"""
# TODO
"""
empty = ()
sigleton = 'hello',
len(empty)
len(sigleton)
print(sigleton)

x, y, z = t


"""
# TODO
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket
'crabgrass' in basket

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)
print(a&b)
print(a^b)

b = {x for x in 'abracadabra' if x not in 'abc'}
print(b)


"""
# TODO
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)


"""
# TODO
"""
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, guido=4127, jack=4098)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.' .format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)


"""
# TODO
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


"""
# TODO
"""
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


"""
# TODO
"""
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


"""
# TODO
"""
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
