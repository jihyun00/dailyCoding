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
append 함수를 통해 list에 값을 계속 추가할 수 있다.
"""
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10))) # 위의 loop 돌아서 집어넣는 것과 동일한 value
squares = [x**2 for x in range(10)] # 위와 동일

[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)


"""
list를 이용하여 아래와 같은 다양한 시도들을 진행할 수 있다.
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
list를 중첩하여 사용할 수 있다.
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

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


"""
zip 함수는 matrix에 있는 원소들의 각 행들의 첫번째 값, 두번째 값... 을 같은 리스트로 묶어서 표현해준다.
"""
print(list(zip(*matrix)))


"""
리스트에서 del 함수를 이용해 값을 지우는 예제
del b[0]을 수행하면 리스트의 첫번째 값이 지워지고, 
b[2:4]를 수행하면 리스트에서 두번째 값부터 세 번째 값까지의 값이 지워진다.
b[:] 는 리스트 전체를 의미하며 del b[:] 수행 시 리스트 b에 있는 값 전체 삭제
"""
b = [-1, 1, 66.25, 333, 333, 1234.5]
del b[0]
print(b)

del b[2:4]
print(b)

del b[:]
print(b)


"""
파이썬에는 tuple이라는 자료구조가 존재한다.
선언은 t = 1234, 234, 'abc' 이런 방식으로 진행
tuple 값 호출은 t[해당 인덱스] 방식으로 호출
"""
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

"""
tuple 간에 중첩도 가능하다.
"""
u = t, (1, 2, 3, 4, 5)
print(u)

"""
tuple은 고정값이기 때문에 t[0]에 새로운 값을 집어넣는 것이 허용되지 않는다.
"""
#t[0] = 88888

"""
tuple에 list도 집어넣을 수 있다.
"""
v = ([1, 2, 3], [3, 2, 1])
print(v)


"""
tuple과 list의 차이는, tuple의 경우 변하지 않고, 다양한 자료형이 들어간다.
list는 종종 변하고, 하나의 자료형으로만 구성되어 있다.

빈 tuple을 선언하고 싶을 때는 empty = () 와 같이 선언해준다.
sigleton = 'hello'로 선언했을 때는 sigleton을 string을 담은 변수로 간주하지만,
sigleton = 'hello', 라 선언하면 tuple로 간주한다.
"""
empty = ()
sigleton = 'hello',
len(empty)
len(sigleton)
print(sigleton)

x, y, z = t


"""
파이썬에는 집합 자료구조도 존재한다. 
집합은 중복이 허용되지 않으며 우리가 알고 있는 집합 연산 모든 것을 허용한다.
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket # result : True
'crabgrass' in basket # result : False

a = set('abracadabra')
b = set('alacazam')
print(a) # 각각 문자를 하나의 원소로 간주, 동일한 값이 여러번 들어왔을 때 하나로 간주
print(a-b) # 차집합
print(a&b) # 합집합
print(a^b) # a나 b에 포함되어 있으나 공통으로 포함되어 있지는 않은 원소들

b = {x for x in 'abracadabra' if x not in 'abc'}
print(b) # a, b, c는 공통으로 포함되어 있으므로 d, r 출력


"""
Dictionary에 대한 자료구조
key, value로 구성되어 있다.
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

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, guido=4127, jack=4098)


"""
looping을 하는 여러 가지 방법들
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v) # key, value값이 차례대로 출력

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v) # 0 tic ....

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.' .format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


"""
isnan 함수를 통해 값의 NaN 여부를 확인할 수 있음
"""
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


"""
python에서 연산은 nested 될 수 있다.
"""
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


"""
여러 타입과 값을 비교할 수 있다.
"""
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
