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

