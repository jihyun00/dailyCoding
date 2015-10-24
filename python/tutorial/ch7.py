"""
value를 string으로 바꾸는 방법
1. str(value)
2. repr(value)

str 함수의 경우 사람이 읽을 수 있는 값으로 리턴
repr 함수의 경우 인터프리터가 해석할 수 있는 값으로 리턴
"""
s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello world\n'
hellos = repr(hello)
print(hellos)

repr((x, y, ('spam', 'eggs')))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end= ' ')
    print(repr(x*x*x).rjust(4))


"""
format 함수를 이용하여 원하는 값을 넣을 수 있다.
"""
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


"""
출력 결과 : We are the knights who say 'Ni'!
"""
print('We are the {} who say "{}!"'.format('knights', 'Ni'))


"""
순서를 명시해주지 않을 경우 format 함수 인자 순서대로 출력
아래와 같이 순서를 명시해 줄 수도 있음.
"""
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))


"""
format에 넘겨주는 인자로 순서대신 값으로 줄 수도 있음
"""
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))


"""
!r 사용시 repr 적용, !a 사용시 ascii, !s는 str
"""
import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

"""
.3f 는 소수점 3자리 까지 표현하겠다는 의미
"""
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

"""
TODO ????
"""
table = {'sjoerd': 4127, 'jack': 4098, 'dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

"""
dict값을 출력하기 위해 [] 로 접근하여 해당값을 출력할 수도 있음. 
혹은 format 함수 인자로 **value 값을 넘겨줘서 출력 가능
"""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};'
      'Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


"""
% value 방식으로도 string을 formatting 할 수 있다.
"""
print('The value of PI is approximately %5.3f.' % math.pi)


"""
파일 접근함수, open 함수를 통해 파일을 연다.
다음 인자로 write 할지(w), read할지(r) 등의 옵션을 결정
"""
f = open('test.txt', 'r+')

val = f.read() # read file
print(val)
val2 = f.read()
print(val2)

line = f.readline()  # read file one line
print(line)
line2 = f.readline()
print(line2)

"""
파일을 끝까지 읽는다.
"""
for line in f:
    print(line, end= ' ')

f.write('This is a test\n') # write file
value = ('the answer', 42)
s = str(value)
f.write(s)

f = open('test.txt', 'wb+') # b는 binary mode로 파일을 엶
f.write(b'234234asdf')
test = f.seek(5) # seek(offset, from_what)
"""
from_what이 0일 경우 file start 지점
1일 경우 현재 위치
2일 경우 file of end
"""
print(test)
f.seek(-3, 2)
f.read(1)

f.close()
#f.read() -> As file closed, this occurs error.

with open('test.txt',  'r') as f:
    read_data = f.read()

f.closed


"""
dumps 함수 수행시 해당 값을 str로 나열
"""
import json

json.dumps([1, 'simple', 'list'])
json.dump(x, f)
x = json.load(f) # load 함수는 해당 value를 json type으로 다시 load
